import datetime
import os
import random

import pytest
from pulp import PULP_CBC_CMD

from mypulp import GRB, LinExpr, Model, lpDot, multidict


def test_sample(snapshot):
    model = Model("lo1")
    J, v = multidict({1: 16, 2: 19, 3: 23, 4: 28})
    x1 = model.addVar(vtype=GRB.CONTINUOUS, name="x1")
    x2 = model.addVar(vtype="C", name="x2")
    x3 = model.addVar(lb=0, ub=30, vtype="C", name="x3")
    model.update()
    model.addSOS(2, [x1, x2, x3])
    L1 = LinExpr([2, 1, 1], [x1, x2, x3])
    model.addConstr(lhs=L1, sense="<=", rhs=60)
    model.addConstr(x1 + 2 * x2 + x3 <= 60)
    model.setObjective(15 * x1 + 18 * x2 + 30 * x3, GRB.MAXIMIZE)
    model.write("mypulp1.mps")
    model.write("mypulp1.lp")
    model.optimize()
    snapshot.assert_match(model.Status)
    snapshot.assert_match(model.ObjVal)
    snapshot.assert_match([(v.VarName, v.X) for v in model.getVars()])
    snapshot.assert_match([(c.ConstrName, c.Pi) for c in model.getConstrs()])
    os.remove("mypulp1.mps")
    os.remove("mypulp1.lp")


def test_option():
    n = 5000
    random.seed(0)
    w = [random.random() + 1 for _ in range(n)]
    p = [random.random() * 0.1 + w[i] for i in range(n)]
    model = Model("knapsack")
    v = [model.addVar(vtype="B", name=f"x{i}") for i in range(n)]
    model.setObjective(lpDot(p, v), GRB.MAXIMIZE)
    model.addConstr(lpDot(w, v) <= int(n * 1.25))
    st = datetime.datetime.now()
    solver = PULP_CBC_CMD(timeLimit=1, msg=1, gapRel=0)
    model.optimize(solver)
    tm = datetime.datetime.now() - st
    assert tm.total_seconds() == pytest.approx(1.15, 0.15)
