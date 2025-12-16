import streamlit as st
import matplotlib.pyplot as plt

# 1. Título e Configuração da Página
st.set_page_config(page_title="Analisador de Primos", page_icon="🔢")
st.title("🔢 Analisador de Primos (Sequência $6n \pm 1$)")

# 2. Entrada de Dados (Substitui o input)
st.sidebar.header("Configurações")
end = st.sidebar.number_input(
    "Ordem final da sequência (n)?", 
    min_value=1, 
    max_value=2000, 
    value=100,
    step=1,
    help="Valores muito altos podem tornar a app lenta."
)

# Botão para iniciar o cálculo (para não correr a cada mudança de número)
if st.sidebar.button("Calcular Primos"):
    
    # Lógica de cálculo (Mantendo a sua lógica original, mas organizada)
    primelst = {2, 3}
    
    # Barra de progresso visual
    progress_bar = st.progress(0)
    
    # Loop 1: 6n - 1
    for n in range(1, end + 1):
        num = 6 * n - 1
        is_prime = True
        # Pequena otimização: checar apenas até a raiz quadrada
        for y in range(2, int(num**0.5) + 1): 
            if num % y == 0:
                is_prime = False
                break
        if is_prime:
            primelst.add(num)
            
    # Loop 2: 6n + 1
    for n in range(1, end + 1):
        num = 6 * n + 1
        is_prime = True
        for y in range(2, int(num**0.5) + 1):
            if num % y == 0:
                is_prime = False
                break
        if is_prime:
            primelst.add(num)
        
        # Atualizar barra de progresso
        progress_bar.progress(n / end)

    # Organização dos dados
    primelstlst = sorted(list(primelst))
    
    # Dicionário para guardar as listas de diferenças
    diff_lists = {
        "Gémeos (Diff 2)": [],
        "Diferença 4": [],
        "Diferença 6": [],
        "Diferença 8": [],
        "Diferença 10": []
    }

    # Análise das diferenças (Loop único para eficiência)
    for x in range(len(primelstlst) - 1):
        diff = primelstlst[x+1] - primelstlst[x]
        pair = (primelstlst[x], primelstlst[x+1])
        
        if diff == 2:
            diff_lists["Gémeos (Diff 2)"].append(pair)
        elif diff == 4:
            diff_lists["Diferença 4"].append(pair)
        elif diff == 6:
            diff_lists["Diferença 6"].append(pair)
        elif diff == 8:
            diff_lists["Diferença 8"].append(pair)
        elif diff == 10:
            diff_lists["Diferença 10"].append(pair)

    # 3. Exibição dos Resultados (Substitui os prints)
    st.success(f"Cálculo concluído! Encontrados {len(primelstlst)} números primos.")
    
    # Exibir métricas em colunas
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Gémeos", len(diff_lists["Gémeos (Diff 2)"]))
    col2.metric("Diff 4", len(diff_lists["Diferença 4"]))
    col3.metric("Diff 6", len(diff_lists["Diferença 6"]))
    col4.metric("Diff 8", len(diff_lists["Diferença 8"]))
    col5.metric("Diff 10", len(diff_lists["Diferença 10"]))

    # Expander para ver a lista completa de primos (para não poluir a tela)
    with st.expander("Ver lista completa de Primos"):
        st.write(primelstlst)

    with st.expander("Ver Pares de Primos Gémeos"):
        st.write(diff_lists["Gémeos (Diff 2)"])

    # 4. Gráfico (Matplotlib integration)
    st.subheader("Gráfico de Lacunas entre Primos Gémeos")
    
    twins = diff_lists["Gémeos (Diff 2)"]
    if len(twins) > 1:
        # A sua lógica de gráfico descomentada e adaptada
        twingap = [twins[x+1][0] - twins[x][0] for x in range(len(twins)-1)]
        x_axis = [x[0] for x in twins[:-1]]
        
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(x_axis, twingap, marker='.', linestyle='-', color='purple', alpha=0.6)
        ax.set_title("Distância entre pares de primos gémeos consecutivos")
        ax.set_xlabel("Valor do Primo")
        ax.set_ylabel("Gap (Distância)")
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        
        # Comando específico do Streamlit para mostrar o gráfico
        st.pyplot(fig)
    else:
        st.warning("Não há dados suficientes de primos gémeos para gerar o gráfico. Aumente a ordem final.")

else:
    st.info("Defina a ordem na barra lateral e clique em 'Calcular Primos' para começar.")
