import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Função para verificar se um número é primo
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Configuração da Página
st.set_page_config(page_title="Números Primos Gémeos", page_icon="👯")

st.title("👯 Números Primos Gémeos")

st.markdown("""
**O que são?**
Os primos gémeos são pares de números primos cuja diferença é exatamente 2.
Exemplos: (3, 5), (5, 7), (11, 13).

A famosa **Conjetura dos Primos Gémeos** diz que existem infinitos pares destes números, mas ninguém conseguiu provar isso ainda!
""")

st.divider()

# Secção 1: Verificador
st.header("🔍 Verificador de Primos Gémeos")
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro Número", min_value=1, value=3, step=1)
with col2:
    num2 = st.number_input("Segundo Número", min_value=1, value=5, step=1)

if st.button("Verificar"):
    # Ordenar para garantir que a diferença é calculada corretamente
    n_min, n_max = sorted([num1, num2])
    
    if is_prime(n_min) and is_prime(n_max) and (n_max - n_min == 2):
        st.success(f"✅ Sim! ({n_min}, {n_max}) são Primos Gémeos!")
    else:
        st.error(f"❌ Não. ({n_min}, {n_max}) não são Primos Gémeos.")
        if not is_prime(n_min):
            st.warning(f"O número {n_min} não é primo.")
        if not is_prime(n_max):
            st.warning(f"O número {n_max} não é primo.")
        if is_prime(n_min) and is_prime(n_max) and (n_max - n_min != 2):
            st.info(f"Ambos são primos, mas a diferença é {n_max - n_min} (deveria ser 2).")

st.divider()

# Secção 2: Gráfico com Matplotlib
st.header("📊 Densidade de Primos Gémeos")
st.write("Vamos visualizar quantos pares de primos gémeos existem até um certo número.")

max_val = st.slider("Limite máximo para análise", 100, 5000, 1000)

if st.checkbox("Gerar Gráfico"):
    primes = [i for i in range(2, max_val) if is_prime(i)]
    twin_primes_count = 0
    counts = []
    x_axis = []

    for i in range(len(primes) - 1):
        if primes[i+1] - primes[i] == 2:
            twin_primes_count += 1
        x_axis.append(primes[i+1])
        counts.append(twin_primes_count)
    
    # Criar o gráfico
    fig, ax = plt.subplots()
    ax.plot(x_axis, counts, color='purple')
    ax.set_title(f"Quantidade de Primos Gémeos até {max_val}")
    ax.set_xlabel("Número Natural")
    ax.set_ylabel("Total de Pares Encontrados")
    ax.grid(True, linestyle='--', alpha=0.6)
    
    st.pyplot(fig)