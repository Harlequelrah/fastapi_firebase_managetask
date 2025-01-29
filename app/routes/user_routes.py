from fastapi import APIRouter, HTTPException
from app.models.user_models import UserCreateModel,UserUpdateModel
from app.firebase import db
user_app=APIRouter(
    prefix="/users",
)
@user_app.post("/users/")
async def create_user(user_data: UserCreateModel):
    try:
        doc_ref = db.collection("users").document()
        user_dict=user_data.dict()
        doc_ref.set(user_dict)
        return {"message": f"User  created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")

@user_app.put("/{user_id}")
async def update_user(user_id: str, user: UserUpdateModel):
    user_data = user.dict(exclude_unset=True)
    doc_ref = db.collection("users").document(user_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="User not found")
    doc_ref.update(user_data)
    return {"message": f"User {user_id} updated successfully"}
