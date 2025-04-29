
def response_user(user,token_access):
    if token_access:
        session_user_data={
        "id": user.id_med_user,
        "usuario": user.st_usuario,
        "Token":token_access
    }
        print(session_user_data)
        return session_user_data

def response_get_pacientes(patient):
    if patient:
        session_pac_data={
            "id": patient.paciente_id,
            "usuario": patient.nombre,
            "apellidos":patient.apellido,
            "Estado":patient.estado_id
            }
        
        return session_pac_data

def response_create_pacientes(nuevop):
    if nuevop:
        session_resp={
            "message": "Paciente registrado con éxito",
            "paciente_id": nuevop.paciente_id
            }
    
    return session_resp