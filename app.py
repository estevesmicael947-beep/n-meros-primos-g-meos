import streamlit as st
import matplotlib.pyplot as plt

def is_prime(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    """Encontra pares de primos gémeos até ao limite."""
    twins = []
    for i in range(2, limit):
        # Primos gémeos são pares (p, p+2) onde ambos são primos
        if is_prime(i) and is_prime(i + 2):
            twins.append((i, i + 2))
    return twins

# --- Configuração da Página ---
st.title("👯‍♀️ Números Primos Gémeos")
st.write("""
**O que são?**
São pares de números primos que diferem em apenas 2 unidades (ex: 3 e 5).
Este site ajuda-te a encontrá-los e visualizar a sua distribuição.
""")

# --- Barra Lateral para Opções ---
st.sidebar.header("Configuração")
limit = st.sidebar.slider("Procurar até ao número:", min_value=10, max_value=200, value=50)

# --- Processamento ---
twin_primes = find_twin_primes(limit)
count = len(twin_primes)

# --- Mostrar Resultados ---
st.subheader(f"Encontrei {count} pares até {limit}:")

# Mostrar em formato de texto
st.write(twin_primes)

# --- Gráfico (Matplotlib) ---
st.subheader("📊 Distribuição Visual")

if count > 0:
    # Vamos extrair apenas os primeiros números de cada par para o gráfico
    x_vals = [p[0] for p in twin_primes]
    y_vals = [p[1] for p in twin_primes]

    fig, ax = plt.subplots()
    ax.scatter(x_vals, y_vals, color='blue', alpha=0.6)
    ax.set_title(f"Pares de Primos Gémeos (até {limit})")
    ax.set_xlabel("Primo P")
    ax.set_ylabel("Primo P + 2")
    ax.grid(True, linestyle='--', alpha=0.7)
    
    st.pyplot(fig)
else:
    st.warning("Nenhum par encontrado com este limite.")
