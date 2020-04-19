Mypulp is a wrapper module for PuLP. It supports to call PuLP using the same functions and classes as in Gurobi, a commercial mixed integer optimization solver.
For more details, see the Gurobi HP http://www.gurobi.com/.
::

    from mypulp import *
    model = Model("lo1")
    J, v = multidict({1:16, 2:19, 3:23, 4:28})
    x1 = model.addVar(vtype=GRB.CONTINUOUS, name="x1")
    x2 = model.addVar(vtype="C", name="x2")
    x3 = model.addVar(lb=0, ub=30, vtype="C", name="x3")
    model.update()
    model.addSOS(2, [x1, x2, x3])
    L1 = LinExpr([2, 1, 1], [x1, x2, x3])
    model.addConstr(lhs=L1, sense="<=", rhs=60)
    model.addConstr(x1 + 2*x2 + x3 <= 60)
    model.setObjective(15*x1 + 18*x2 + 30*x3, GRB.MAXIMIZE)
    model.write("mypulp1.mps")
    model.write("mypulp1.lp")
    model.optimize()
    if model.Status == GRB.Status.OPTIMAL:
        print("Opt. Value =", model.ObjVal)
        for v in model.getVars():
            print(v.VarName, v.X)
        for c in model.getConstrs():
            print(c.ConstrName, c.Pi)

Requirements
------------
* Python 3.7, pulp

Features
--------
* nothing

Setup
-----
::

   $ pip install pulp
   $ pip install mypulp

History
-------
* 0.0.1 (2015-05-04) first release
* 0.0.8 (2016-02-03)
