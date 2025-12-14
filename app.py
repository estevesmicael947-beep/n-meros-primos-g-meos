import streamlit as st
import matplotlib.pyplot as plt

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Primos Gémeos", page_icon="🇵🇹")

st.title("Investigação de Primos Gémeos (6n ± 1)")
st.write("Defina um limite para $n$ e analise a distribuição dos números primos e os seus intervalos.")

# --- DADOS DE ENTRADA ---
end = st.number_input("Valor final para n (na sequência 6n+1):", min_value=10, max_value=50000, value=100, step=10)

# --- BOTÃO DE EXECUÇÃO ---
if st.button("Iniciar Cálculo"):
    
    # Barra de progresso
    bar = st.progress(0)
    status = st.empty()
    status.text("A calcular números primos...")
    
    # --- LÓGICA MATEMÁTICA ---
    primelst = {2, 3}
    
    # Gerar primos da forma 6n-1
    n = 1
    while n <= end:
        num = 6 * n - 1
        y = 2
        is_prime = True
        while y * y <= num:
            if num % y == 0:
                is_prime = False
                break
            else:
                y += 1
        if is_prime:
            primelst.add(num)
        n += 1
    
    bar.progress(50)

    # Gerar primos da forma 6n+1
    n = 1    
    while n <= end:
        num = 6 * n + 1
        y = 2
        is_prime = True
        while y * y <= num:
            if num % y == 0:
                is_prime = False
                break
            else:
                y += 1
        if is_prime:
            primelst.add(num)
        n += 1
            
    bar.progress(100)
    status.empty()

    # --- CLASSIFICAÇÃO DOS INTERVALOS ---
    primelstlst = sorted(list(primelst))
    
    twins = []  # Dif. 2
    fours = []  # Dif. 4
    sixes = []  # Dif. 6
    eights = [] # Dif. 8
    tens = []   # Dif. 10

    for x in range(len(primelstlst)-1):
        diff = primelstlst[x+1] - primelstlst[x]
        pair = (primelstlst[x], primelstlst[x+1])
        
        if diff == 2: twins.append(pair)
        elif diff == 4: fours.append(pair)
        elif diff == 6: sixes.append(pair)
        elif diff == 8: eights.append(pair)
        elif diff == 10: tens.append(pair)

    # --- APRESENTAÇÃO DOS RESULTADOS ---
    st.success(f"Cálculo terminado! Foram encontrados {len(primelstlst)} números primos.")
    
    # Métricas Principais
    col1, col2 = st.columns(2)
    col1.metric("Total de Primos", len(primelstlst))
    col2.metric("Primos Gémeos (Dif. 2)", len(twins))
    
    # Métricas Secundárias (Nomes corrigidos para PT)
    col3, col4, col5 = st.columns(3)
    col3.metric("Primos com Dif. 4", len(fours))
    col4.metric("Primos com Dif. 6", len(sixes))
    col5.metric("Primos com Dif. 8", len(eights))

    st.write("---")
    
    # O Gráfico
    st.subheader("Gráfico de Distribuição dos Intervalos")
    
    x_axis = [primelstlst[x] for x in range(len(primelstlst)-1)]
    y_axis = [primelstlst[x+1]-primelstlst[x] for x in range(len(primelstlst)-1)]
    
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x_axis, y_axis, '.', markersize=3, color='blue', alpha=0.6, label="Intervalo")
    
    # Linha de destaque para os Gémeos
    ax.axhline(y=2, color='r', linestyle='--', linewidth=0.8, label="Nível dos Gémeos (2)")
    
    ax.set_title("Variação da Diferença entre Primos Consecutivos")
    ax.set_xlabel("Número Primo")
    ax.set_ylabel("Tamanho do Intervalo (Gap)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)

    # Listas Detalhadas
    st.subheader("Listas Detalhadas de Pares")
    
    with st.expander("Ver Primos Gémeos (Diferença de 2)"):
        st.write(twins)
    with st.expander("Ver Primos com Diferença de 4"):
        st.write(fours)
    with st.expander("Ver Primos com Diferença de 6"):
        st.write(sixes)
    with st.expander("Ver Primos com Diferença de 8"):
        st.write(eights)
    with st.expander("Ver Primos com Diferença de 10"):
        st.write(tens)
