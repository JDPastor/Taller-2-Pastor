from pgmpy . models import BayesianNetwork
from pgmpy . factors . discrete import TabularCPD

model = BayesianNetwork ([("C", "A") , ("U", "A") ])


cpd_c = TabularCPD(variable="C", variable_card=3, values=[[0.33], [0.33], [0.33]])
cpd_u = TabularCPD(variable="U", variable_card=3, values=[[0.33], [0.33], [0.33]])

cpd_a = TabularCPD(
    variable="A",
    variable_card=3,
    values=[
        [0, 0, 0, 0, 0.5, 1, 0, 1, 0.5],
        [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5],
        [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0],
    ],
    evidence=["C", "U"],
    evidence_card=[3, 3],
)

model.add_cpds(cpd_c, cpd_u, cpd_a)

model.check_model()


from pgmpy.inference import VariableElimination

infer = VariableElimination(model)

posterior_p = infer.query(["C"], evidence={"U": 0, "A": 2})
print(posterior_p)

##Caso 2

posterior_p = infer.query(["C"], evidence={"U": 2, "A": 1})
print(posterior_p)

##Caso 3

posterior_p = infer.query(["C"], evidence={"U": 2})
print(posterior_p)


##Caso 4

posterior_p = infer.query(["C"], evidence={"A": 2})
print(posterior_p)


print(model.get_independencies())
