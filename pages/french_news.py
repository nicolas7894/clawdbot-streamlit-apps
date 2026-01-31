import streamlit as st
import feedparser
from datetime import datetime

# Page config
st.set_page_config(page_title="Actualités France", page_icon="🇫🇷", layout="wide")

st.title("🇫🇷 Actualités France")
st.markdown("Les dernières nouvelles des principaux médias français")

# French news RSS feeds
NEWS_SOURCES = {
    "Le Monde": "https://www.lemonde.fr/rss/une.xml",
    "Le Figaro": "https://www.lefigaro.fr/rss/figaro_actualites.xml",
    "France 24": "https://www.france24.com/fr/rss",
    "France Info": "https://www.francetvinfo.fr/titres.rss",
    "Libération": "https://www.liberation.fr/arc/outboundfeeds/rss-all/collection/accueil/?outputType=xml",
    "BFMTV": "https://www.bfmtv.com/rss/news-24-7/",
}

@st.cache_data(ttl=300)
def fetch_news(feed_url, source_name):
    """Fetch and parse RSS feed"""
    try:
        feed = feedparser.parse(feed_url)
        articles = []
        for entry in feed.entries[:10]:  # Get top 10 articles
            article = {
                "title": entry.get("title", "Sans titre"),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", entry.get("description", "")),
                "published": entry.get("published", "Date inconnue"),
            }
            articles.append(article)
        return articles
    except Exception as e:
        st.error(f"Erreur lors du chargement de {source_name}: {e}")
        return []

# Sidebar for source selection
st.sidebar.header("📰 Sources")
selected_sources = []
for source in NEWS_SOURCES.keys():
    if st.sidebar.checkbox(source, value=True):
        selected_sources.append(source)

st.sidebar.markdown("---")
st.sidebar.info("Les actualités sont actualisées toutes les 5 minutes.")

if not selected_sources:
    st.warning("Veuillez sélectionner au moins une source d'actualités dans la barre latérale.")
else:
    # Create tabs for sources
    tabs = st.tabs(selected_sources)
    
    for tab, source_name in zip(tabs, selected_sources):
        with tab:
            feed_url = NEWS_SOURCES[source_name]
            articles = fetch_news(feed_url, source_name)
            
            if not articles:
                st.info(f"Aucun article disponible pour {source_name} pour le moment.")
            else:
                for article in articles:
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        
                        with col1:
                            st.markdown(f"### [{article['title']}]({article['link']})")
                            # Clean summary (remove HTML tags)
                            summary = article['summary'].replace('<p>', '').replace('</p>', '').replace('<br>', '\n')
                            if len(summary) > 300:
                                summary = summary[:300] + "..."
                            st.markdown(f"*{summary}*")
                        
                        with col2:
                            st.caption(f"📅 {article['published']}")
                        
                        st.markdown("---")

# Footer
st.markdown("---")
st.caption("📡 Données récupérées via les flux RSS officiels des médias | Made with Streamlit 🇫🇷")
