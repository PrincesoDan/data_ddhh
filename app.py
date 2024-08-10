import streamlit as st


def main():
    _, bigcol, _ = st.columns([1, 10, 1])
    with bigcol:
        st.title("Detenidos desaparecidos en Chile durante la dictadura de Pinochet")