import streamlit as st
import json

st.title("AI App Generator")

user_input = st.text_input("Enter your app idea")

if st.button("Generate"):

    intent = {
        "app_type": user_input,
        "features": [
            "login",
            "dashboard",
            "database"
        ]
    }

    design = {
        "entities": [
            "User",
            "Admin"
        ],
        "roles": [
            "admin",
            "user"
        ],
        "flows": [
            "authentication",
            "data management"
        ]
    }

    schema = {
        "db_schema": {
            "users": [
                "id",
                "name",
                "email"
            ]
        },
        "api": {
            "endpoint": "/users"
        },
        "ui": {
            "pages": [
                "login",
                "dashboard"
            ]
        }
    }

    final_output = {
        "intent_extraction": intent,
        "system_design": design,
        "schema_generation": schema
    }

    st.json(final_output)