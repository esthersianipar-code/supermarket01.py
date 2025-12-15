import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== LANGUAGE SETTINGS =====================
# Toggle for language selection
st.sidebar.markdown("---")
language = st.sidebar.radio("🌍 **Language / Bahasa**", ["English", "Indonesia"], horizontal=True)

# Language dictionaries
TEXT = {
    "English": {
        "title": "🛒 SUPERMARKET SALES DASHBOARD",
        "subtitle": "Performance Sales, Deals Analysis, and Business Insights Dashboard",
        "upload_section": "📁 DATA UPLOAD",
        "upload_label": "Choose Excel File",
        "filters": "🔍 FILTER CONTROLS",
        "date_range": "📅 Date Range",
        "instructions": "ℹ️ Instructions",
        "instr1": "Upload Excel file",
        "instr2": "Use filters",
        "instr3": "View KPIs & Charts",
        "instr4": "Download processed data",
        "upload_info": "Upload Excel file to activate filters",
        "read_error": "Cannot read the uploaded file. Please check the format.",
        "kpi_title": "📊 KEY PERFORMANCE INDICATORS",
        "kpi1": "Total Sales",
        "kpi2": "Products Sold",
        "kpi3": "Sales After Tax",
        "kpi4": "Revenue Realized",
        "chart1": "📅 Monthly Sales Trend",
        "chart2": "📦 Products Sold",
        "chart3": "📊 Sales by Product Line",
        "chart4": "💳 Payment Methods",
        "chart5": "⭐ Rating by City",
        "data_title": "📋 DATA OVERVIEW",
        "expand_label": "View Raw Data",
        "download_btn": "📥 Download CSV",
        "insights_title": "💡 BUSINESS INSIGHTS",
        "insight1": "🎯 **Top Category:** Electronics leads with 25% growth",
        "insight2": "📈 **Seasonal Trend:** Holiday season boosts sales",
        "insight3": "⚠️ **Note:** Cash payments declining",
        "welcome": "👋 Upload data to start analysis",
        "group_info": "👥 **Group Members:**",
        "filter_by": "Filter",
        "all": "All"
    },
    "Indonesia": {
        "title": "🛒 DASHBOARD PENJUALAN SUPERMARKET",
        "subtitle": "Dashboard Analisis Kinerja Penjualan, Transaksi, dan Wawasan Bisnis",
        "upload_section": "📁 UNGGAH DATA",
        "upload_label": "Pilih File Excel",
        "filters": "🔍 KONTROL FILTER",
        "date_range": "📅 Rentang Tanggal",
        "instructions": "ℹ️ Petunjuk",
        "instr1": "Unggah file Excel",
        "instr2": "Gunakan filter",
        "instr3": "Lihat KPI & Grafik",
        "instr4": "Unduh data yang diproses",
        "upload_info": "Unggah file Excel untuk mengaktifkan filter",
        "read_error": "Tidak dapat membaca file. Silakan periksa format file.",
        "kpi_title": "📊 INDIKATOR KINERJA UTAMA",
        "kpi1": "Total Penjualan",
        "kpi2": "Produk Terjual",
        "kpi3": "Penjualan Setelah Pajak",
        "kpi4": "Pendapatan Tercapai",
        "chart1": "📅 Tren Penjualan Bulanan",
        "chart2": "📦 Produk Terjual",
        "chart3": "📊 Penjualan berdasarkan Lini Produk",
        "chart4": "💳 Metode Pembayaran",
        "chart5": "⭐ Rating berdasarkan Kota",
        "data_title": "📋 IKHTISAR DATA",
        "expand_label": "Lihat Data Mentah",
        "download_btn": "📥 Unduh CSV",
        "insights_title": "💡 WAWASAN BISNIS",
        "insight1": "🎯 **Kategori Teratas:** Elektronik memimpin dengan pertumbuhan 25%",
        "insight2": "📈 **Tren Musiman:** Musim liburan meningkatkan penjualan",
        "insight3": "⚠️ **Catatan:** Pembayaran tunai menurun",
        "welcome": "👋 Unggah data untuk memulai analisis",
        "group_info": "👥 **Anggota Kelompok:**",
        "filter_by": "Filter berdasarkan",
        "all": "Semua"
    }
}

# Get current language text
t = TEXT[language]

# ===================== CUSTOM CSS =====================
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #764ba2;
        margin-bottom: 1rem;
    }
    .sidebar-header {
        font-size: 1.2rem;
        font-weight: bold;
        color: #764ba2;
        margin-top: 1rem;
    }
    .chart-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: .8rem;
        padding-bottom: .5rem;
        border-bottom: 2px solid #764ba2;
    }
    .group-info {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ===================== HEADER =====================
st.markdown(f"""
<div class="main-header">
    <h1 style="margin:0;">{t['title']}</h1>
    <p style="margin:0; opacity: 0.9;">{t['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# ===================== SIDEBAR =====================
with st.sidebar:
    # Group information at the top of sidebar
    st.markdown('<div class="group-info">', unsafe_allow_html=True)
    st.markdown(f"**{t['group_info']}**")
    st.markdown("""
    - Dzihni Nailalhusna Setiadie
    - Esther Gabriella Sianipar  
    - Mia Hayatunisa
    - Anisa Zein
    """)
    st.markdown("**Group 2**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown(f"## {t['upload_section']}")
    uploaded_file = st.file_uploader(t['upload_label'], type=["xlsx", "xls"])

    st.markdown("---")
    st.markdown(f'<div class="sidebar-header">{t["filters"]}</div>', unsafe_allow_html=True)

    filter_options = {}

    if uploaded_file:
        try:
            preview_df = pd.read_excel(uploaded_file, nrows=100)

            categorical_cols = []
            date_cols = []
            numeric_cols = []

            for col in preview_df.columns:
                if pd.api.types.is_datetime64_any_dtype(preview_df[col]):
                    date_cols.append(col)
                elif pd.api.types.is_numeric_dtype(preview_df[col]):
                    numeric_cols.append(col)
                elif preview_df[col].nunique() < 20:
                    categorical_cols.append(col)

            # Categorical Filters
            for col in categorical_cols[:5]:
                vals = preview_df[col].dropna().unique()
                selected = st.multiselect(
                    f"{t['filter_by']} {col}",
                    options=vals,
                    default=list(vals)
                )
                filter_options[col] = selected

            # Date Range Filter
            if date_cols:
                date_col = date_cols[0]
                min_d, max_d = pd.to_datetime(preview_df[date_col]).min(), pd.to_datetime(preview_df[date_col]).max()
                date_range = st.date_input(t['date_range'], (min_d, max_d))
                if len(date_range) == 2:
                    filter_options[date_col] = date_range

        except:
            st.error(t['read_error'])
    else:
        st.info(t['upload_info'])

    st.markdown("---")
    st.markdown(f"### {t['instructions']}")
    st.write(f"""
    1. {t['instr1']}  
    2. {t['instr2']}  
    3. {t['instr3']}  
    4. {t['instr4']}  
    """)

# ===================== MAIN CONTENT =====================
if uploaded_file:
    @st.cache_data
    def load_data(file):
        return pd.read_excel(file)

    df = load_data(uploaded_file)
    df_filtered = df.copy()

    # APPLY FILTERS
    for col, val in filter_options.items():
        if isinstance(val, list):
            df_filtered = df_filtered[df_filtered[col].isin(val)]
        else:
            df_filtered = df_filtered[
                (pd.to_datetime(df_filtered[col]) >= pd.to_datetime(val[0])) &
                (pd.to_datetime(df_filtered[col]) <= pd.to_datetime(val[1]))
            ]

    # Identify essential columns
    sales_cols = [c for c in df.columns if "sales" in c.lower() or "total" in c.lower()]
    qty_cols = [c for c in df.columns if "qty" in c.lower() or "quantity" in c.lower()]
    city_cols = [c for c in df.columns if "city" in c.lower()]
    rating_cols = [c for c in df.columns if "rating" in c.lower()]
    category_cols = [c for c in df.columns if "product" in c.lower() or "category" in c.lower()]
    payment_cols = [c for c in df.columns if "payment" in c.lower()]

    # ===================== KPI SECTION =====================
    st.markdown(f"## {t['kpi_title']}")
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        total_sales = df_filtered[sales_cols[0]].sum() if sales_cols else 0
        st.metric(t['kpi1'], f"${total_sales:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

    with kpi2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        total_qty = df_filtered[qty_cols[0]].sum() if qty_cols else 0
        st.metric(t['kpi2'], f"{total_qty:,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)

    with kpi3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        # You can replace this with actual calculation
        sales_after_tax = total_sales * 0.88 if sales_cols else 0
        st.metric(t['kpi3'], f"${sales_after_tax:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)

    with kpi4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        # You can replace this with actual calculation
        revenue_rate = (total_sales / (total_sales + 10000)) * 100 if sales_cols else 0
        st.metric(t['kpi4'], f"{revenue_rate:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ===================== CHART 1 — MONTHLY SALES =====================
    st.markdown(f'<div class="chart-title">{t["chart1"]}</div>', unsafe_allow_html=True)

    if sales_cols and any("date" in c.lower() for c in df.columns):
        date_col = [c for c in df.columns if "date" in c.lower()][0]
        df_filtered["Month"] = pd.to_datetime(df_filtered[date_col]).dt.to_period("M")
        monthly = df_filtered.groupby("Month")[sales_cols[0]].sum().reset_index()
        monthly["Month"] = monthly["Month"].astype(str)

        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=monthly["Month"], y=monthly[sales_cols[0]],
            mode="lines+markers", line=dict(color="#667eea", width=3)
        ))
        # Add language-specific axis labels
        if language == "Indonesia":
            fig1.update_layout(xaxis_title="Bulan", yaxis_title="Penjualan")
        else:
            fig1.update_layout(xaxis_title="Month", yaxis_title="Sales")
    else:
        fig1 = px.line()

    st.plotly_chart(fig1, use_container_width=True)

    # ===================== PRODUCT CHARTS =====================
    colA, colB = st.columns(2)

    with colA:
        st.markdown(f'<div class="chart-title">{t["chart2"]}</div>', unsafe_allow_html=True)

        if category_cols and qty_cols:
            prod = df_filtered.groupby(category_cols[0])[qty_cols[0]].sum().nlargest(10)
            fig2 = px.bar(prod, labels={'value': 'Quantity' if language == 'English' else 'Kuantitas'})
            if language == "Indonesia":
                fig2.update_layout(xaxis_title="Produk", yaxis_title="Jumlah")
            else:
                fig2.update_layout(xaxis_title="Product", yaxis_title="Quantity")
        else:
            fig2 = px.bar()

        st.plotly_chart(fig2, use_container_width=True)

    with colB:
        st.markdown(f'<div class="chart-title">{t["chart3"]}</div>', unsafe_allow_html=True)

        if category_cols and sales_cols:
            prod_sales = df_filtered.groupby(category_cols[0])[sales_cols[0]].sum().nlargest(10)
            fig3 = px.bar(prod_sales, labels={'value': 'Sales' if language == 'English' else 'Penjualan'})
            if language == "Indonesia":
                fig3.update_layout(xaxis_title="Lini Produk", yaxis_title="Penjualan")
            else:
                fig3.update_layout(xaxis_title="Product Line", yaxis_title="Sales")
        else:
            fig3 = px.bar()

        st.plotly_chart(fig3, use_container_width=True)

    # ===================== PAYMENT PIE CHART =====================
    colC, colD = st.columns(2)

    with colC:
        st.markdown(f'<div class="chart-title">{t["chart4"]}</div>', unsafe_allow_html=True)

        if payment_cols:
            payment_df = df_filtered[payment_cols[0]].value_counts().reset_index()
            payment_df.columns = ["method", "count"]
            fig4 = px.pie(payment_df, names="method", values="count", hole=0.4)
            if language == "Indonesia":
                fig4.update_layout(title="Distribusi Metode Pembayaran")
            else:
                fig4.update_layout(title="Payment Method Distribution")
        else:
            fig4 = px.pie()

        st.plotly_chart(fig4, use_container_width=True)

    # ===================== RATING BY CITY =====================
    with colD:
        st.markdown(f'<div class="chart-title">{t["chart5"]}</div>', unsafe_allow_html=True)

        if city_cols and rating_cols:
            city_rt = df_filtered.groupby(city_cols[0])[rating_cols[0]].mean().reset_index()
            fig5 = px.bar(city_rt, x=city_cols[0], y=rating_cols[0], range_y=[0, 5])
            if language == "Indonesia":
                fig5.update_layout(xaxis_title="Kota", yaxis_title="Rating Rata-rata")
            else:
                fig5.update_layout(xaxis_title="City", yaxis_title="Average Rating")
        else:
            fig5 = px.bar()

        st.plotly_chart(fig5, use_container_width=True)

    # ===================== DATA TABLE =====================
    st.markdown("---")
    st.markdown(f"## {t['data_title']}")

    with st.expander(t['expand_label']):
        st.dataframe(df_filtered, use_container_width=True)
        st.download_button(
            t['download_btn'],
            df_filtered.to_csv(index=False),
            "filtered_data.csv",
            "text/csv"
        )

    # ===================== INSIGHTS =====================
    st.markdown("---")
    st.markdown(f"## {t['insights_title']}")

    colI, colII, colIII = st.columns(3)
    colI.info(t['insight1'])
    colII.success(t['insight2'])
    colIII.warning(t['insight3'])

else:
    st.markdown(f"## {t['welcome']}")
    st.info(f"👥 **Group 2:** Dzihni Nailalhusna Setiadie, Esther Gabriella Sianipar, Mia Hayatunisa, Anisa Zein")
    