# CLI Naming Convention — Forgeflow (`ff`)

Este documento define la **convención oficial de naming** para el CLI de Forgeflow (`forgeflow` / `ff`).
Su objetivo es asegurar **claridad semántica**, **consistencia**, **escalabilidad** y una **buena experiencia de uso (UX)** a medida que el CLI crece.

---

## Objetivos del naming

* Claridad: el comando debe entenderse sin documentación adicional.
* Consistencia: patrones repetibles y predecibles.
* Escalabilidad: el naming no se rompe al agregar nuevos dominios o acciones.
* Ergonomía: permitir aliases cortos sin perder semántica.
* Profesionalismo: alineado con CLIs consolidados (git, kubectl, docker).

---

## Estructura base del CLI

```
ff <dominio> <acción> [opciones]
```

* **Dominio**: sustantivo → qué cosa se está manipulando.
* **Acción**: verbo → qué se hace con esa cosa.
* **Opciones**: modificadores del comportamiento.

---

## 1. Naming de dominios (grupos)

### Reglas

* Sustantivos.
* Singular.
* `kebab-case`.
* Representan un **objeto conceptual**, no un proceso.
* No repetir información implícita.

### Convención

| Elemento            | Regla             |
| ------------------- | ----------------- |
| Nombre canónico     | Largo y explícito |
| Alias               | Corto pero claro  |
| Cantidad de aliases | Máximo **1**      |

### Ejemplos

| Canónico              | Alias       | Evaluación   |
| --------------------- | ----------- | ------------ |
| `structure`           | `struct`    | ✅ correcto   |
| `schema`              | `sch`       | ❌ críptico   |
| `directory-structure` | `structure` | ❌ redundante |

**Regla práctica:**
Si el dominio ya es corto y claro, **no necesita alias**.

---

## 2. Naming de acciones (comandos)

### Reglas

* Verbos en infinitivo implícito.
* `kebab-case`.
* Expresivos y específicos.
* Una acción = un solo significado.

### Convención

| Elemento            | Regla                                |
| ------------------- | ------------------------------------ |
| Nombre canónico     | Verbo + contexto                     |
| Alias               | Verbo corto con el mismo significado |
| Cantidad de aliases | Máximo **1**                         |

### Ejemplo principal

| Canónico           | Alias       | Evaluación                          |
| ------------------ | ----------- | ----------------------------------- |
| `create-from-json` | `from-json` | ✅ excelente                         |
| `generate`         | `gen`       | ⚠ solo si el contexto es inequívoco |
| `process`          | `proc`      | ❌ ambiguo                           |

**Regla crítica:**
El alias **no debe introducir una nueva interpretación** de la acción.

---

## 3. Relación dominio–acción

> El comando **no debe repetir el dominio**.

❌ Incorrecto:

```
ff structure create-structure-from-json
```

✅ Correcto:

```
ff structure create-from-json
```

El dominio ya define el contexto.

---

## 4. Naming de opciones (`--flags`)

### Reglas

* Siempre `--kebab-case`.
* Sustantivos o adjetivos.
* Nunca verbos.
* Evitar abreviaciones crípticas.

### Ejemplos

| Correcto    | Incorrecto     | Motivo       |
| ----------- | -------------- | ------------ |
| `--schema`  | `--sch`        | Críptico     |
| `--root`    | `--r`          | Poco legible |
| `--json`    | `--input-json` | Redundante   |
| `--dry-run` | `--test`       | Ambiguo      |

**Regla:**
Los flags **no llevan alias cortos por defecto**.
Solo se justifican en comandos de uso intensivo.

---

## 5. Política de aliases

### Permitido

* Aliases para ergonomía.
* Aliases obvios y consistentes.
* Aliases que no cambian la semántica.

### No permitido

* Más de 1 alias por dominio o acción.
* Aliases “creativos” o no obvios.
* Aliases documentados como primarios.
* Aliases con significado distinto al canónico.

---

## 6. Documentación

### Documentación oficial (canónica)

```bash
forgeflow structure create-from-json --json tree.json --schema fs.schema.json
```

### Nota secundaria

> Alias disponibles: `struct`, `from-json`

### Nunca documentar como ejemplo principal

```bash
ff struct from-json
```

Los aliases son **azúcar sintáctica**, no contrato público.

---

## 7. Ejemplo completo (estado ideal)

```bash
forgeflow structure create-from-json --json tree.json --schema fs.schema.json

ff struct from-json --json tree.json --schema fs.schema.json
```

Misma semántica. Diferente ergonomía.

---

## 8. Checklist para aceptar un nuevo comando

Antes de agregar un comando, debe cumplir:

* [ ] El dominio es un sustantivo claro.
* [ ] La acción es un verbo inequívoco.
* [ ] No repite el dominio.
* [ ] Tiene máximo 1 alias.
* [ ] El alias no cambia el significado.
* [ ] El nombre largo es el documentado.

Si falla uno → **no se acepta**.

---

## Conclusión

Esta convención:

* Reduce deuda semántica.
* Protege la coherencia del CLI.
* Escala sin romper UX.
* Trata el CLI como **producto**, no como script.

Debe considerarse **normativa** para Forgeflow.

---

## Siglas y conceptos

| Término    | Definición                                      |
| ---------- | ----------------------------------------------- |
| CLI        | Command Line Interface                          |
| UX         | User Experience                                 |
| Alias      | Nombre alternativo que ejecuta el mismo comando |
| Dominio    | Grupo que representa un objeto conceptual       |
| Acción     | Comando que ejecuta una operación               |
| Kebab-case | Formato con guiones (`create-from-json`)        |
| DRY        | Don’t Repeat Yourself                           |





