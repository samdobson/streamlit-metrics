import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Template

def _build_metric(label, value):
    html_text = """
    <style>
    .metric {
       font-family: "IBM Plex Sans", sans-serif;
       text-align: center;
    }
    .metric .value {
       font-size: 48px;
       line-height: 1.6;
    }
    .metric .label {
       letter-spacing: 2px;
       font-size: 14px;
       text-transform: uppercase;
    }

    </style>
    <div class="metric">
       <div class="value">
          {{ value }}
       </div>
       <div class="label">
          {{ label }}
       </div>
    </div>
    """
    html = Template(html_text)
    return html.render(label=label, value=value)

def metric_row(data):
    columns = st.beta_columns(len(data))
    for i, (label, value) in enumerate(data.items()):
        with columns[i]:
            components.html(_build_metric(label, value))

def metric(label, value):
    components.html(_build_metric(label, value))
