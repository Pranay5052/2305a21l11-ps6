import streamlit as st
st.title("2305A21L11-PS6")
st.write("Calculate the Efficiency of the transformer and copper losses at various loads")

def Tran_Eff(va,cl,fcl,k,pf):
    eff=(k*va*pf)*100/(k*va*pf+cl+k**2*fcl)
    cul=k**2*fcl
    return eff,cul

col1,col2=st.columns(2)
with col1:
    va=st.number_input("Rating of transformer(VA):", value=5)
    cl=st.number_input("Core Losses(W):", value=50)
    fcl=st.number_input("Full Load Copper Losses(W):", value=100)
    k=st.number_input("Loading of transformer(0-1):",value=0.5)
    pf=st.number_input("Power Factor(0-1):",value=0.8)
    compute=st.button("compute")
with col2:
    with st.container(border=True):
        if compute:
            eff,cul=Tran_Eff(va,cl,fcl,k,pf)
            st.write(f"Efficiency of Transformer={eff:.2f} %")
            st.write(f"Copper losses of Trasformer={cul:.2f} Watts")
                

