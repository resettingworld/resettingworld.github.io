import json
import os
import zipfile

with open('data/marketplace_catalog.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

CATEGORY_MAP = {
    # Supervivència i Resiliència
    'supervivencia-es': 'Supervivència i Resiliència',
    'control-de-plagas': 'Supervivència i Resiliència',
    'cultiu-interior-hidroponia': 'Supervivència i Resiliència',
    'jardineria-horticultura-urbana': 'Supervivència i Resiliència',
    'compostatge-fertilitat-sol': 'Supervivència i Resiliència',
    'permacultura-agroecologia': 'Supervivència i Resiliència',
    'agricultura-general-i-sostenible': 'Supervivència i Resiliència',
    'gutenberg-health-medicine': 'Supervivència i Resiliència',
    'gutenberg-earth-agricultural-sciences': 'Supervivència i Resiliència',
    'gutenberg-practical-manuals-how-to': 'Supervivència i Resiliència',

    # Ciència i Coneixement Humà
    'gutenberg-physics': 'Ciència i Coneixement Humà',
    'gutenberg-chemistry-biochemistry': 'Ciència i Coneixement Humà',
    'gutenberg-mathematics': 'Ciència i Coneixement Humà',
    'gutenberg-engineering-technology': 'Ciència i Coneixement Humà',
    'gutenberg-economics': 'Ciència i Coneixement Humà',
    'gutenberg-research-methods-information-systems': 'Ciència i Coneixement Humà',
    'ciencias-de-la-tierra': 'Ciència i Coneixement Humà',
    'ciencias-aplicadas': 'Ciència i Coneixement Humà',
    'ciencias-naturales': 'Ciència i Coneixement Humà',
    'ciencias-sociales': 'Ciència i Coneixement Humà',
    'textos-info-ciencia': 'Ciència i Coneixement Humà',
    'textos-info-historia': 'Ciència i Coneixement Humà',
    'textos-info-ensayo': 'Ciència i Coneixement Humà',
    'textos-info-tratado': 'Ciència i Coneixement Humà',
    'planetalibro-ciencia': 'Ciència i Coneixement Humà',
    'planetalibro-historia': 'Ciència i Coneixement Humà',
    'planetalibro-ensayo': 'Ciència i Coneixement Humà',
    'planetalibro-economia': 'Ciència i Coneixement Humà',

    # Filosofia i Pensament Crític
    'textos-info-filosofia': 'Filosofia i Pensament',
    'textos-info-politica': 'Filosofia i Pensament',
    'planetalibro-filosofia': 'Filosofia i Pensament',
    'planetalibro-politica': 'Filosofia i Pensament',
    'planetalibro-estrategia': 'Filosofia i Pensament',
}

enriched = []
for it in items:
    cid = it['id']
    cat = CATEGORY_MAP.get(cid, 'Tecnologia i Informàtica')
    is_survival = (
        cat == 'Supervivència i Resiliència'
        or 'supervivencia' in cid
        or 'plaga' in cid
        or 'cultiu' in cid
        or 'agri' in cid
        or 'health' in cid
    )

    enriched.append({
        **it,
        'portal_category': cat,
        'is_survival': is_survival,
        'install_command': f"smart-local import-pack {it['file']}",
        'rag_id': cid,
        'cover_image': f"static/covers/{cid}.jpg",
        'release_url': f"https://github.com/resettingworld/catalogo/releases/download/v1.0.0/{it['file']}",
        'catalogo_path': f"https://github.com/resettingworld/catalogo/tree/main/catalogs/{cid}",
    })

enriched.sort(key=lambda x: (not x['is_survival'], x['portal_category'], -x['books_count']))

with open('web/static/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(enriched, f, indent=2, ensure_ascii=False)

with open('web/static/catalog.js', 'w', encoding='utf-8') as f:
    f.write('window.RW_CATALOG = ' + json.dumps(enriched, ensure_ascii=False) + ';\n')

print(f"Generated web/static/catalog.json & catalog.js with {len(enriched)} packs.")
