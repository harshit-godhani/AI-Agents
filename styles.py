STYLES = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
    --primary-gradient: linear-gradient(135deg, #0077B6, #023E8A);
    --secondary-gradient: linear-gradient(135deg, #00B4D8, #0077B6);
    --primary-color: #000000;
    --secondary-color: #B3E5FC;
    --text-color: #000000;
    --card-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
    --hover-shadow: 0 12px 28px rgba(0, 0, 0, 0.20);
    --border-radius: 12px;
    --transition-speed: 0.4s;
}

    body {
        margin: 0;
        padding: 0;
    }

    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        background-image: url('https://images.unsplash.com/photo-1708724195876-1156245fce21?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        backdrop-filter: blur(5px);
        color: var(--text-color);
    }

    @media (prefers-color-scheme: dark) {
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1586525063813-9d9e35081bc5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        }
    }

    .main-header {
        font-size: 2.6rem;
        font-weight: 700;
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: centercolor: var(--primary-color);
        background: none;
        -webkit-background-clip: initial;
        -webkit-text-fill-color: initial;;
        margin: 1.5rem 0;
        padding-bottom: 1.5rem;
        border-bottom: 2px solid rgba(255, 255, 255, 0.2);
        letter-spacing: -0.03em;
    }

    .sub-header {
        font-size: 2rem;
        font-weight: 700;
        color: var(--secondary-color);
        background: none;
        -webkit-background-clip: initial;
        -webkit-text-fill-color: initial;
        margin: 2rem 0 1.2rem;
        padding-bottom: 0.6rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.15);
        text-transform: capitalize;
        letter-spacing: 0.5px;
        line-height: 1.3;
    }

    .card {
        border-radius: var(--border-radius);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        background: rgba(255, 255, 255, 0.25);
        color: var(--text-color);
        box-shadow: var(--card-shadow);
        backdrop-filter: blur(12px) saturate(180%);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: transform var(--transition-speed) ease, box-shadow var(--transition-speed) ease;
    }

    .card:hover {
        transform: translateY(-6px) scale(1.02);
        box-shadow: var(--hover-shadow);
    }

    .hotel-card {
        background: rgba(255, 255, 255, 0.08);
        border-left: 5px solid var(--primary-color);
    }

    .travel-card {
        background: rgba(255, 255, 255, 0.06);
        border-left: 5px solid var(--secondary-color);
    }

    .travel-card-selected {
        background: rgba(255, 255, 255, 0.1);
        border-left: 5px solid var(--primary-color);
        box-shadow: var(--hover-shadow);
    }

    .hotel-name {
        font-size: 1.4rem;
        font-weight: 700;
        color: var(--primary-color);
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
    }

    .hotel-name::before {
        content: "";
        width: 10px;
        height: 10px;
        background-color: var(--primary-color);
        border-radius: 50%;
        margin-right: 0.6rem;
    }

    .hotel-detail {
        color: var(--text-color);
        font-weight: 400;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
    }

    .status-box {
        padding: 1.1rem;
        border-radius: var(--border-radius);
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        box-shadow: var(--card-shadow);
        margin-bottom: 1.5rem;
        color: #000000;
    }

    .status-box:hover {
        transform: translateY(-2px);
        box-shadow: var(--hover-shadow);
    }

    .info-box {
        background: rgba(255, 255, 255, 0.25);
        border-left: 4px solid #000000;
    }

    .warning-box {
        background: rgba(255, 193, 7, 0.08);
        border-left: 4px solid #FFC107;
    }

    .error-box {
        background: rgba(244, 67, 54, 0.08);
        border-left: 4px solid #F44336;
    }

    .icon-text {
        display: flex;
        align-items: center;
        margin-bottom: 0.6rem;
        color: var(--text-color);
    }

    .icon-text:hover {
        transform: translateX(4px);
    }

    .icon-text svg {
        margin-right: 0.6rem;
        color: var(--primary-color);
    }

    .travel-mode-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--primary-color);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }

    .travel-mode-title svg {
        transition: transform 0.3s ease;
    }

    .travel-mode-title:hover svg {
        transform: scale(1.1);
    }

    .travel-mode-title span {
        margin-left: 0.6rem;
    }

    .travel-stat {
        font-size: 1rem;
        margin-bottom: 0.6rem;
        border-bottom: 1px dashed rgba(255, 255, 255, 0.1);
        padding: 0.4rem 0;
        color: var(--text-color);
    }

    .travel-value {
        font-weight: 600;
        color: var(--primary-color);
        background: rgba(255, 255, 255, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 4px;
        margin-left: 0.4rem;
    }

    .sidebar-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--primary-color);
        background: none;
        -webkit-background-clip: initial;
        -webkit-text-fill-color: initial;
        margin-bottom: 1rem;
        border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    }

    .sidebar-section {
        margin-bottom: 2rem;
        padding-bottom: 2rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stMarkdown, .stText {
        animation: fadeIn 0.4s ease-out;
    }

    button[kind="primary"] {
        background: var(--primary-gradient) !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
        box-shadow: 0 4px 10px rgba(63, 81, 181, 0.25) !important;
        transition: 0.3s all ease !important;
    }

    button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(63, 81, 181, 0.3) !important;
    }

    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: var(--primary-color);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #B3E5FC;
    }

    section[data-testid="stSidebar"] {
        background-image: url('https://images.unsplash.com/photo-1743558011565-8e1ef02e1e5d?q=80&w=2127&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        backdrop-filter: blur(4px);
        color: white;
        position: relative;
    }

    section[data-testid="stSidebar"]::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.4);
        z-index: 0;
        border-radius: 0 12px 12px 0;
    }

    section[data-testid="stSidebar"] > * {
        position: relative;
        z-index: 1;
    }

    /* ✅ Integrated Input Box Styling */
    input[type="text"] {
        color: #000000 !important;
        background-color: rgba(255, 255, 255, 0.85) !important;
        border: 1px solid #ccc !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1rem !important;
    }

    input::placeholder {
        color: #555555 !important;
        font-weight: 500 !important;
    }
</style>
"""
