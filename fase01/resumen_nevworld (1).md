# Resumen de validación — NevWorld
### Organizado según el orden de salida del script

---

## Ejercicio 1 — Nombre del archivo JSON

| Campo | Valor |
|---|---|
| Archivo | `nevworld_209292370141445760_20261005_182702.jsonl` |

---

## Ejercicio 2 — Número total de eventos

| Campo | Valor |
|---|---|
| Total de eventos | `4647` |

---

## Ejercicio 3 — Número de columnas

| Campo | Valor |
|---|---|
| Número de columnas | `36` |

---

## Ejercicio 4 — Nombre de las columnas

`schema_version`, `run_id`, `seed`, `event_index`, `tick`, `type`, `started_at_utc`, `building_id`, `building_type`, `cell_x`, `cell_y`, `width`, `height`, `villager_id`, `activity`, `resource_type`, `amount_before`, `amount_after`, `amount_delta`, `population`, `constructed_buildings`, `wood_stock`, `food_stock`, `gold_stock`, `day`, `prey_type`, `actor_id`, `target_id`, `interaction_type`, `topic`, `relationship_actor_to_target_after`, `relationship_target_to_actor_after`, `need_type`, `state`, `name`, `age`

---

## Ejercicio 5 — Tipo del primer evento registrado

| Campo | Valor |
|---|---|
| Primer evento | `simulation_started` |

---

## Ejercicio 6 — Tipo de evento más frecuente

| Campo | Valor |
|---|---|
| Evento más frecuente | `villager_activity_changed` |
| Cantidad | `3202` |

---

## Ejercicio 7 — Recuento de todos los tipos de eventos

| Tipo de evento | Cantidad |
|---|---:|
| `villager_activity_changed` | 3202 |
| `construction_abandoned` | 354 |
| `social_interaction` | 338 |
| `villager_need_changed` | 248 |
| `world_snapshot` | 218 |
| `resource_changed` | 174 |
| `villager_drank` | 48 |
| `villager_ate` | 38 |
| `building_created` | 14 |
| `construction_expired` | 7 |
| `hunt_completed` | 2 |
| `villager_created` | 2 |
| `simulation_started` | 1 |
| `age_changed` | 1 |
| **Total** | **4647** |

---

## Ejercicio 8 — Identificación de la ejecución (run)

| Campo | Valor |
|---|---|
| run_id | `20261005_182702_209292370141445760_1eee76c4573349018f9aa2847a500435` |
| Semilla | `209292370141445760` |
| Esquema | `2` |

---

## Ejercicio 9 — Rango de ticks

| Campo | Valor |
|---|---|
| Primer tick | `0` |
| Último tick | `130800` |

---

## Ejercicio 10 — Validación final

| Campo | Valor |
|---|---|
| Estado | ✅ **OK** |

---

## Preguntas

**1. ¿Qué te permite afirmar el recuento sobre tu partida? ¿Por qué el tipo más frecuente no tiene que ser el más importante?**

Que puedo inspeccional los eventos que van sucediendo en la partida y cualquier dato sobre ellos. Debido a que el tipo mas frecuente es debido a los cambios constantes de las actividades de los personajes.

**2. ¿Por qué una celda vacía no significa necesariamente que el registro esté mal?**

Porque segun el tipo de evento que sea, algunos tendra unos campos necesarios y otro al no tener esos campos necesarios no es necesario que los tengas ni significa que este mal.

**3. ¿Qué sabes ahora del archivo y qué pregunta sobre tu partida necesitaría un análisis posterior?**

Pues se los datos basicos como el nombre numero de eventes, numero de columnas que tiene, cual es el evento mas reptido y la cantidad, si el dataset es correcto o tiene algun fallo y algunos datos mas sobre los eventos que ha habido en la partida.

Para un analisis posterior necesitaria cuantas personas han nacido, cuantas han muerto, que rol de personaje es el que mas predomina y muchas mas
