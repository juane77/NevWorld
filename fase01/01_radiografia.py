from pathlib import Path

import pandas as pd

DATASET = Path(
    'data/raw/nevworld_209292370141445760_20261005_182702.jsonl'
)

if not DATASET.exists():
    raise FileNotFoundError(
        f'No se encuentra: {DATASET.resolve()}'
    )

df = pd.read_json(DATASET, lines=True)

print('\nNombre del archivo JSON:', DATASET.name)

filas, columnas = df.shape

print('\nNumero total de eventos del JSON: ', filas)


print('\nNumero de columnas: ', columnas)


print('\nNombre de las columnas:', df.columns.tolist())


print('\nTipo del primer evento registrado:', df['type'].iloc[0])


recuento_tipos = df['type'].value_counts()
evento_mas_frecuente = recuento_tipos.idxmax()
cantidad_evento_mas_frecuente = recuento_tipos.max()

print('\nTipo del evento mas frecuente y cantidad registrado:',evento_mas_frecuente,', Cantidad de veces:',cantidad_evento_mas_frecuente)


print('\nRecuento de todos los tipos de eventos: ',df['type'].value_counts())


print('\nrun_id:', df['run_id'].iloc[0])
print('semilla:', df['seed'].iloc[0])
print('esquema:', df['schema_version'].iloc[0])


print('\nprimer tick:', df['tick'].min())
print('último tick:', df['tick'].max())


required = [
    'run_id', 'event_index', 'tick', 'type'
]

assert not df.empty, 'El dataset esta vacio'
assert all(column in df.columns for column in required), \
    'Faltan columnas principales'
assert not df.duplicated(['run_id', 'event_index']).any(), \
    'Hay eventos duplicados'

ordered = df.sort_values('event_index')
assert ordered['tick'].is_monotonic_increasing, \
    'Los ticks retroceden'

print('\nVALIDACIÓN ESTADO: OK')


