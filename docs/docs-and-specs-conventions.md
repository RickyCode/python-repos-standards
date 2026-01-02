# Documentación: Convenciones para `/docs` y `/specs`

## Versión del documento

* **Versión:** 1.0
* **Fecha última actualización:** 2025-09-30
* **Estado:** Activo
* **Criterio de actualización:** Se actualiza cuando se agregan nuevos tipos de documentación o especificaciones formales.

---

## 1. Objetivo

Definir de manera explícita las **características, responsabilidades y convenciones de nombres** para los directorios `/docs` y `/specs`, garantizando coherencia, claridad y mantenibilidad del repositorio.

---

## 2. Público objetivo

* Desarrolladores del proyecto.
* Arquitectos y mantenedores.
* Colaboradores que agreguen documentación o especificaciones.

---

## 3. Alcance

### Incluye

* Definición del propósito de `/docs` y `/specs`.
* Tipos de archivos permitidos.
* Convenciones de nombres.
* Criterios de uso.

### Fuera de alcance

* Contenido específico de cada documento.
* Herramientas de validación o linting.
* Estructura interna de código.

---

## 4. Terminología y siglas

| Término    | Definición                                        |
| ---------- | ------------------------------------------------- |
| Docs       | Documentación orientada a lectura humana          |
| Specs      | Especificaciones formales consumibles por tooling |
| Convención | Regla obligatoria de nombrado o estructura        |
| Canonical  | Forma principal y oficial                         |

---

## 5. Directorio `/docs`

### 5.1 Propósito

Almacenar **documentación orientada a humanos**, destinada a explicar, guiar y contextualizar el proyecto.

---

### 5.2 Características de los archivos

* Formato principal: **Markdown (`.md`)**.
* Lenguaje descriptivo y normativo.
* Prioridad en legibilidad y comprensión inmediata.
* No consumidos directamente por tooling.
* Pueden evolucionar con mayor frecuencia.

---

### 5.3 Tipos de contenido permitidos

* Guías de uso.
* Convenciones y reglas humanas.
* Arquitectura y decisiones (ADR).
* Onboarding y contribución.
* Políticas internas documentadas.

---

### 5.4 Convenciones de nombres

**Regla general:**

* Usar `kebab-case`.
* Nombres descriptivos y explícitos.
* Evitar abreviaciones crípticas.

**Ejemplos válidos:**

* `cli-naming-rules.md`
* `architecture-overview.md`
* `contribution-guidelines.md`

**Ejemplos no válidos:**

* `naming.md`
* `doc1.md`
* `rules_cli.md`

---

## 6. Directorio `/specs`

### 6.1 Propósito

Almacenar **especificaciones formales**, tratadas como **contratos técnicos**, potencialmente consumibles por herramientas, validadores o pipelines.

---

### 6.2 Características de los archivos

* Formatos estructurados: **YAML (`.yml`) y JSON (`.json`)**.
* Contenido declarativo y verificable.
* Alta estabilidad esperada.
* Fuente de verdad para validaciones automáticas.
* Versionables y extensibles.

---

### 6.3 Tipos de contenido permitidos

* Especificaciones de naming.
* Políticas técnicas declarativas.
* Reglas consumidas por linters.
* Schemas de validación.
* Definiciones contractuales del sistema.

---

### 6.4 Convenciones de nombres

**Regla general:**

* Usar **namespacing con puntos**.
* Mantener paridad entre spec y schema.
* Un archivo = una responsabilidad.

**Formato:**

```
<ámbito>.<tema>.<extensión>
```

**Ejemplos válidos:**

* `cli.naming.yml`
* `cli.naming.schema.json`
* `api.auth.yml`
* `api.auth.schema.json`

**Ejemplos no válidos:**

* `cli-naming.yml`
* `naming.yaml`
* `spec1.json`

---

## 7. Relación entre `/docs` y `/specs`

| Aspecto           | `/docs`     | `/specs`          |
| ----------------- | ----------- | ----------------- |
| Público principal | Humanos     | Tooling + humanos |
| Formato           | Markdown    | YAML / JSON       |
| Estabilidad       | Media       | Alta              |
| Rol               | Explicativo | Contractual       |
| Enforcement       | Manual      | Automático        |

---

## 8. Regla fundamental

> Todo aquello que **debe cumplirse por código** pertenece a `/specs`.
> Todo aquello que **debe comprenderse por personas** pertenece a `/docs`.

---

## 9. Consistencia y control

* No duplicar información entre `/docs` y `/specs`.
* `/docs` puede **referenciar** `/specs`, pero no redefinirlas.
* Las especificaciones son la **fuente de verdad** técnica.

---

## 10. Conclusión

Esta separación permite:

* Reducir ambigüedad.
* Escalar el proyecto sin fricción.
* Diferenciar claramente **documentación** de **contrato técnico**.
* Facilitar automatización y gobierno del repositorio.



