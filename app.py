import streamlit as st
import matplotlib.pyplot as plt

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Primos Gémeos", page_icon="🔢")

st.title("Pesquisa de Primos Gémeos (6n ± 1)")
st.write("Insira um número limite e veja o algoritmo a funcionar.")

# --- INPUT DO UTILIZADOR ---
end = st.number_input("Ordem final da sequência (6n+1):", min_value=10, max_value=50000, value=100, step=10)

# --- BOTÃO DE EXECUÇÃO ---
if st.button("Executar Código"):
    
    # Barra de progresso e texto de status
    bar = st.progress(0)
    status = st.empty()
    status.text("A calcular...")
    
    # --- A TUA LÓGICA MATEMÁTICA ---
    primelst = {2, 3}
    
    # Gerar 6n-1
    n = 1
    while n <= end:
        num = 6 * n - 1
        y = 2
        is_prime = True
        # Otimização (y*y <= num) para o site não bloquear
        while y * y <= num:
            if num % y == 0:
                is_prime = False
                break
            else:
                y += 1
        if is_prime:
            primelst.add(num)
        n += 1
    
    bar.progress(50) # 50% concluído

    # Gerar 6n+1
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
            
    bar.progress(100) # 100% concluído
    status.empty()

    # --- CLASSIFICAÇÃO DOS GAPS (A TUA LÓGICA) ---
    primelstlst = sorted(list(primelst))
    
    twins = []  # Gap 2
    fours = []  # Gap 4
    sixes = []  # Gap 6
    eights = [] # Gap 8
    tens = []   # Gap 10

    for x in range(len(primelstlst)-1):
        diff = primelstlst[x+1] - primelstlst[x]
        pair = (primelstlst[x], primelstlst[x+1])
        
        if diff == 2: twins.append(pair)
        elif diff == 4: fours.append(pair)
        elif diff == 6: sixes.append(pair)
        elif diff == 8: eights.append(pair)
        elif diff == 10: tens.append(pair)

    # --- MOSTRAR RESULTADOS NO SITE ---
    st.success(f"Cálculo concluído! Encontrados {len(primelstlst)} primos.")
    
    # 1. Métricas (Números grandes)
    col1, col2 = st.columns(2)
    col1.metric("Total de Primos", len(primelstlst))
    col2.metric("Pares Gémeos (Gap 2)", len(twins))
    
    col3, col4, col5 = st.columns(3)
    col3.metric("Gap 4 (Cousin)", len(fours))
    col4.metric("Gap 6 (Sexy)", len(sixes))
    col5.metric("Gap 8", len(eights))

    st.write("---")
    
    # 2. O Gráfico (Matplotlib)
    st.subheader("Gráfico dos Intervalos")
    
    x_axis = [primelstlst[x] for x in range(len(primelstlst)-1)]
    y_axis = [primelstlst[x+1]-primelstlst[x] for x in range(len(primelstlst)-1)]
    
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x_axis, y_axis, '.', markersize=3, color='blue', alpha=0.6)
    
    # Adicionar uma linha vermelha no Gap 2 para destacar os gémeos
    ax.axhline(y=2, color='r', linestyle='--', linewidth=0.5, label="Gémeos")
    
    ax.set_title("Variação dos Gaps entre Primos")
    ax.set_xlabel("Número Primo")
    ax.set_ylabel("Tamanho do Gap")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)

    # 3. Listas Detalhadas (Expansíveis)
    st.subheader("Listas Detalhadas")
    with st.expander("Ver Primos Gémeos (Gap 2)"):
        st.write(twins)
    with st.expander("Ver Primos Cousin (Gap 4)"):
        st.write(fours)
    with st.expander("Ver Primos Sexy (Gap 6)"):
        st.write(sixes)
    with st.expander("Ver Gap 8"):
        st.write(eights)
    with st.expander("Ver Gap 10"):
        st.write(tens)
