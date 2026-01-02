# Documentación: Guidelines Normativos para Humanos y Agentes IA

**Versión:** 1.0  
**Última actualización:** 2026-01-01  
**Estado:** Activo  

---

## Objetivo

Definir qué son los guidelines, cómo deben diseñarse y cuándo deben usarse, para garantizar alineación de comportamiento en humanos y agentes de inteligencia artificial sin introducir rigidez innecesaria.

---

## Alcance

**Aplica a:**
- Lineamientos de estilo, formato, estructura y restricciones semánticas.
- Uso en documentación, generación de contenido y prompts para agentes IA.
- Sistemas donde el objetivo es guiar comportamiento y calidad.

**No aplica a:**
- Contratos formales entre sistemas.
- Validación automática en pipelines CI/CD.
- Definición de interfaces técnicas ejecutables.

---

## Público Objetivo

- Arquitectos de software y datos.
- Diseñadores de prompts y sistemas con agentes IA.
- Equipos que definen estándares internos de generación y documentación.

---

## Definición de Guidelines

Los guidelines son reglas normativas orientativas que guían el comportamiento esperado sin imponer validación estricta ni contractual. Su función principal es alinear decisiones, estilo y resultados.

---

## Principios Fundamentales

1. **Naturaleza normativa**  
   Usar lenguaje imperativo y reglas explícitas. Evitar sugerencias implícitas.

2. **Control blando**  
   Guiar el comportamiento sin exigir cumplimiento binario.

3. **Compatibilidad humana y con IA**  
   Ser comprensibles para humanos y fácilmente inyectables en prompts.

4. **Independencia de implementación**  
   No depender de herramientas, lenguajes o entornos específicos.

5. **Plasticidad**  
   Permitir adaptación contextual sin perder intención.

---

## Cuándo Usar Guidelines

**Usar guidelines cuando:**
- Se requiera alinear estilo, formato o comportamiento.
- Se controle generación de contenido por IA.
- Se busque consistencia sin validación automática.
- Se definan restricciones semánticas generales.

**No usar guidelines cuando:**
- Se requiera rechazo automático de resultados.
- Se necesite validación determinística.
- Exista un contrato técnico entre componentes.

---

## Relación con Specs

Los guidelines no son specs.

**Diferencias clave:**
- Los guidelines orientan; las specs validan.
- Los guidelines son heurísticos; las specs son determinísticos.
- Los guidelines no rompen flujos; las specs imponen cumplimiento.

**Buenas prácticas:**
- Mantener guidelines como capa base.
- Derivar specs solo para casos que requieran validación automática.
- No reemplazar guidelines por specs de forma general.

---

## Estructura Recomendada de un Guideline

- Objetivo claro.
- Reglas explícitas y numeradas.
- Lenguaje imperativo.
- Alcance definido.
- Exclusiones claras.
- Ausencia de justificaciones o explicaciones innecesarias.

---

## Ejemplo

**Regla correcta:**  
> No usar HTML ni Markdown.

**Regla incorrecta:**  
> Se recomienda evitar HTML cuando sea posible.

---

## Criterios de Actualización

**Actualizar guidelines cuando:**
- Se detecte ambigüedad recurrente.
- Cambie el objetivo de alineación.
- Se agreguen nuevos contextos de uso.

**No actualizar guidelines para:**
- Ajustes puntuales de implementación.
- Casos excepcionales o aislados.

---

## Consistencia y Versionado

- Mantener una versión explícita.
- Registrar fecha de última actualización.
- Evitar contradicciones entre documentos.
- Unificar terminología entre todos los guidelines.

---

## Definiciones y Siglas

| Término | Definición |
|------|-----------|
| Guideline | Regla normativa orientativa que guía comportamiento |
| Spec | Especificación formal, verificable y contractual |
| Regla normativa | Regla expresada como obligación |
| Control blando | Mecanismo de alineación no determinístico |
| LLM | Large Language Model |
| Prompt | Instrucción entregada a un modelo de lenguaje |
| Heurística | Regla práctica no estrictamente formal |
| Determinismo | Propiedad de producir siempre el mismo resultado ante el mismo input |
| Idempotencia | Propiedad de producir el mismo efecto aunque la operación se repita |
