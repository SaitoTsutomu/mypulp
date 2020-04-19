# from mypulp import *
# m=Model()
#
#
# x = [0,2,3,1]
# y = [1,0,3,3]
#
# n=len(x)
#
# X=m.addVar(ub=3.0, name="X")
# Y=m.addVar(ub=3.0, name ="Y")
#
# Z=m.addVar(name ="Z")
#
# a,b={},{}
# for i in range(n):
#     a[i] =m.addVar(name="a({0})".format(i))
#     b[i] =m.addVar(name="b({0})".format(i))
#     m.update()
#
# for i in range(n):
#     m.addConstr( a[i] >= x[i] -X )
#     m.addConstr( a[i] >= X-x[i] )
#     m.addConstr( b[i] >= y[i] -Y )
#     m.addConstr( b[i] >= Y-y[i] )
#
#     m.addConstr(Z>=a[i]+b[i])
#
# m.setObjective(Z, GRB.MINIMIZE)
# # m.setObjective( quicksum( 1*a[i] for i in range(n))
# #                + quicksum( 1*b[i] for i in range(n)), GRB.MINIMIZE )
#
#
# m.optimize()
#
# print(X.X,Y.X)
# print(m.ObjVal)
# for i in range(n):
#     print(a[i].X,b[i].X)

# model = Model("lo1")
#
# x = model.addVar(name='tonkoke')
# y = model.addVar(name='kokenton')
# z = model.addVar(name='mix')
#
# #model.setObjective(15*x + 18*y + 30*z, GRB.MAXIMIZE)
# model.addConstr(2*x +   y + z <= 60, name='pork')
# model.addConstr(  x + 2*y + z <= 60, name='chicken')
# model.addConstr(            z <= 30, name='beef')
#
# model.optimize()
# print( model.ObjVal )
# for i in model.getVars():
#     print(i.VarName, i.X)

model = Model("lo1")

J, v = multidict({1: 16, 2: 19, 3: 23, 4: 28})

# x1 = model.addVar(vtype="C", name="x1")
# x2 = model.addVar(vtype="I", name="x2")
# x3 = model.addVar(lb=0, ub=30, vtype="B", name="x3")

x1 = model.addVar(vtype=GRB.CONTINUOUS, name="x1")
# x1 = model.addVar(vtype="N", lb=10.5, ub=50,name="x1")
x2 = model.addVar(vtype="C", name="x2")
x3 = model.addVar(lb=0, ub=30, vtype="C", name="x3")

model.update()
model.addSOS(2, [x1, x2, x3])
L1 = LinExpr([2, 1, 1], [x1, x2, x3])
# L1=LinExpr()
# L1.addTerms(2,x1)
# L1.addTerms(1,x2)
# L1.addTerms(1,x3)

# model.addConstr(lhs=L1,sense="<=",rhs=60,name="C0")
# model.addConstr(x1 + 2*x2 + x3 <= 60, name="C1")

c1 = model.addConstr(lhs=L1, sense="<=", rhs=60)
model.addConstr(x1 + 2 * x2 + x3 <= 60)

model.setObjective(15 * x1 + 18 * x2 + 30 * x3, GRB.MAXIMIZE)

# relax=model.relax()
# model.sos1= { 1:{x1:1,x2:2} }
model.write("mypulp1.mps")
model.write("mypulp1.lp")
model.optimize()

if model.Status == GRB.Status.OPTIMAL:
    model.write("answer.sol")
    print("Opt. Value=", model.ObjVal)
    # for v in model.getVars():
    #    print(v.VarName,v.X,v.RC)
    for v in model.getVars():
        print(v.VarName, v.X)
    for c in model.getConstrs():
        print(c.ConstrName, c.Pi)
# m=Model()
# x=m.addVar( name="x", vtype="I" , lb=1)
# y=m.addVar( name="y", vtype="I" , lb=1)
# z=m.addVar( name="z", vtype="I" , lb=1)
# m.update()
# m.addConstr(2*x+ y ==11)
# m.addConstr(y+ 3*z ==14)
# # m.setObjective(0,GRB.MINIMIZE)
# m.optimize()
# print(x.X,y.X,z.X)
