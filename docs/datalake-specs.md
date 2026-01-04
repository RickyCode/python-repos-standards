# Data Lake Specifications – Diseño y Gobernanza

**Versión:** 1.0
**Estado:** Activo
**Última actualización:** 2026-01-02
**Audiencia:** Arquitectura de datos, Data Engineering, Analytics Engineering

---

## 1. Objetivo

Definir las **especificaciones normativas** para el diseño, organización y evolución de un Data Lake corporativo.

---

## 2. Alcance

Incluye:

* Definición de capas
* Contratos de datos
* Convenciones
* Lineamientos de modelado
* Estrategia de consumo

Fuera de alcance:

* Implementación tecnológica
* Herramientas específicas
* Casos de uso particulares

---

## 3. Terminología

* Data Lake
* Modelo Medallón
* Data Contract
* Modelo Estrella
* Datamart

---

## 4. Estructura de Specs Propuesta

```
data-lake-spec/
├─ scope.yaml
├─ layers/
│  ├─ bronze.yaml
│  ├─ silver.yaml
│  └─ gold.yaml
├─ conventions.yaml
├─ data-contracts/
├─ quality-rules.yaml
├─ modeling-guidelines.yaml
├─ security.yaml
└─ consumption.yaml
```

### 4.1 `scope.yaml`

Define:

* Objetivo del Data Lake
* Casos de uso soportados
* Casos explícitamente no soportados

Uso:

* Marco de referencia
* Control de expansión indebida

---

### 4.2 `layers/bronze.yaml`

Define:

* Qué se considera dato crudo
* Reglas de ingestión
* Retención
* Inmutabilidad

Regla:

> Bronze no aplica reglas de negocio.

---

### 4.3 `layers/silver.yaml`

Define:

* Limpieza
* Tipificación
* Relaciones
* Modelos analíticos base

Incluye:

* Modelos estrella
* Dimensiones conformadas

---

### 4.4 `layers/gold.yaml`

Define:

* Datamarts
* Sábanas por reporte
* Agregaciones permitidas

Regla:

> Gold optimiza consumo, no integra dominios.

---

### 4.5 `data-contracts/`

Define, por fuente:

* Esquema
* Tipos
* Campos obligatorios
* Evolución permitida

Formato recomendado:

* YAML versionado

---

### 4.6 `conventions.yaml`

Define:

* Naming
* Claves
* Fechas
* Zonas horarias
* Versionado

Uso obligatorio.

---

### 4.7 `quality-rules.yaml`

Define:

* Validaciones por capa
* Nullability
* Duplicados
* Rangos

Regla:

> Cada capa incrementa el nivel de exigencia.

---

### 4.8 `modeling-guidelines.yaml`

Define:

* Cuándo usar modelo estrella
* Cuándo usar sábanas
* Manejo de SCD
* Compartición de dimensiones

---

### 4.9 `security.yaml`

Define:

* Clasificación de datos
* Accesos por capa
* Principios de mínimo privilegio

---

### 4.10 `consumption.yaml`

Define:

* Quién consume cada capa
* Herramientas autorizadas
* Contratos de salida

---

## 5. Versionado y mantenimiento

* Cambios requieren PR
* Cambios estructurales incrementan versión mayor
* Cambios semánticos incrementan versión menor

---

## 6. Regla final

> Un Data Lake sin specs es solo almacenamiento.
> Las specs definen el sistema, no la tecnología.

---

## Glosario de siglas y conceptos

| Término             | Definición                        |
| ------------------- | --------------------------------- |
| **DW**              | Data Warehouse corporativo        |
| **Datamart**        | Subconjunto analítico por dominio |
| **Data Lake**       | Almacenamiento analítico central  |
| **Modelo Medallón** | Bronze–Silver–Gold                |
| **Modelo Estrella** | Hechos + dimensiones              |
| **Data Contract**   | Contrato de esquema y semántica   |
| **SCD**             | Slowly Changing Dimension         |
| **BI**              | Business Intelligence             |

Si quieres, el siguiente paso natural es:
👉 **convertir esta documentación en un repo base con plantillas listas para usar.**
