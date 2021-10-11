db.define_table("gentes",
    Field("Nombre", type="string"),
    Field("Apellido", type="string"),
    Field("Edad", type="integer")
)

@auth.requires_login()

def gente():
    return{"grid":SQLFORM.grid(db.gentes)}

def user():
    return{"form":auth()}

def index():
    redirect(URL("gente"))