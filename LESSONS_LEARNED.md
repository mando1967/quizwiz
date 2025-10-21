# QuizWiz Development - Lessons Learned

*Last Updated: 2025-10-19*

This document captures important lessons learned during QuizWiz development to avoid repeating mistakes and improve future development efficiency.

---

## 1. JSON & LaTeX Integration

### Issue
LaTeX commands in JSON files were not rendering correctly.

### Solution
- **Double-escape backslashes in JSON**: Use `\\` for LaTeX commands
  - Example: `$\\mathbf{F}_2$`, `$\\approx$`, `$\\theta_x$`
- JSON parser treats `\` as escape character, so `\\` becomes `\` in the actual string

### Critical: Display Math Blocks Need Blank Lines
When using multiple consecutive display math blocks (`$$...$$`), you **MUST** separate them with blank lines (`\n\n`):

**❌ WRONG (breaks rendering):**
```json
{
  "explanation": "## Step 2\n\n$$A = \\\\int_{0}^{4} f(x)\\\\,dx$$\n$$A = \\\\left[F(x)\\\\right]_{0}^{4}$$\n$$A = F(4) - F(0)$$"
}
```

**✅ CORRECT:**
```json
{
  "explanation": "## Step 2\n\n$$A = \\\\int_{0}^{4} f(x)\\\\,dx$$\n\n$$A = \\\\left[F(x)\\\\right]_{0}^{4}$$\n\n$$A = F(4) - F(0)$$"
}
```

### Continuation Format (Alternative)
For multi-step equations, use continuation format (no blank lines needed):
```json
{
  "explanation": "$$\\\\bar{X} = \\\\frac{1}{A}\\\\int_{0}^{4} x f(x)\\\\,dx$$\n$$= \\\\frac{1}{A}\\\\left[F(x)\\\\right]_{0}^{4}$$\n$$= \\\\frac{1}{A}(F(4) - F(0))$$"
}
```
Note: Subsequent lines start with `=` (continuation), not the variable name.

### Best Practice
- Always use double backslashes for LaTeX in JSON files
- Add blank lines (`\n\n`) between separate display math blocks
- Use continuation format (`$$=...$$`) for multi-step derivations
- Test rendering immediately after adding LaTeX content

---

## 2. Markdown Parser Integration with MathJax

### Issue
Adding marked.js for Markdown parsing broke LaTeX rendering and caused undefined errors.

### Solution
1. **Load order matters**: Load marked.js synchronously before MathJax
   ```html
   <script src="marked.min.js"></script>
   <script defer src="mathjax.js"></script>
   ```

2. **Always validate before parsing**:
   ```javascript
   typeof marked !== 'undefined' && marked.parse && content ? marked.parse(content) : (content || '')
   ```

3. **Separate concerns**: Only parse Markdown in explanations, not in short answer fields with LaTeX

### Best Practice
- Check library existence AND method existence before calling
- Never pass `undefined` or `null` to parsing functions
- Provide fallback values with `|| ''`

---

## 3. Array Validation in JavaScript

### Issue
Empty arrays (`[]`) are truthy in JavaScript, causing logic errors.

### Solution
Check for both existence AND length:
```javascript
if (data.choices && data.choices.length > 0) {
  // Process choices
}
```

### Best Practice
For arrays, always check `.length > 0`, not just truthiness.

---

## 4. Quiz Type Detection

### Issue
Code assumed all quizzes were multiple-choice, causing errors for free-response questions.

### Solution
Distinguish between quiz types:
- **Multiple-choice**: `choices.length > 0`
- **Free-response**: `choices.length === 0` or no choices array

Only show selection validation for multiple-choice questions.

### Best Practice
Design code to handle multiple question formats from the start. Don't assume data structure.

---

## 5. URL Encoding for File Paths

### Issue
Paths with spaces (e.g., "CE 333/Test 1") failed to load.

### Solution
```javascript
const encodedPath = path.split('/').map(segment => encodeURIComponent(segment)).join('/');
```

Encode each segment separately, preserving path structure and query strings.

### Best Practice
Always URL-encode user-generated or dynamic path segments, but preserve delimiters and query strings.

---

## 6. Configuration-Driven UI Elements

### Issue
"Wizard Mode" button appeared for single-test subjects where it wasn't useful.

### Solution
Make UI elements conditional based on config:
```javascript
if (testSet.tutorPath) {
  // Show Wizard Mode button
}
```

### Best Practice
Tie UI element visibility to configuration data, not hardcoded logic.

---

## 7. Incremental Testing Strategy

### Issue
Multiple changes made at once made debugging difficult.

### Solution
- Test after each significant change
- Use browser console to catch errors immediately
- Verify with actual production data, not test data

### Best Practice
Make small, testable changes. Verify each change works before moving to the next.

---

## 8. Plain Text vs Rendered Content

### Issue
Answers displayed as plain text instead of rendered LaTeX/Markdown.

### Solution
- Use LaTeX syntax (`$...$`) for math in answer fields
- Use Markdown syntax (`##`) for structure in explanations
- Ensure MathJax processes entire card after rendering

### Best Practice
Separate formatting concerns: LaTeX for math, Markdown for structure, HTML for layout.

---

## General Development Principles

1. **Validate all inputs** - Check for existence, type, and content before processing
2. **Fail gracefully** - Provide fallbacks for missing libraries or data
3. **Test with real data** - Don't assume data structure; test with actual production data
4. **Load order matters** - Dependencies must load before code that uses them
5. **Escape appropriately** - Different contexts (JSON, HTML, URLs) require different escaping
6. **Check the console** - Browser console errors provide exact line numbers and error types
7. **Empty != Missing** - Empty arrays/strings exist but are "empty"; check both existence and content

---

## Quick Reference: Common Patterns

### Safe Markdown Parsing
```javascript
const parsed = (typeof marked !== 'undefined' && marked.parse && content) 
  ? marked.parse(content) 
  : (content || '');
```

### Safe Array Processing
```javascript
if (array && array.length > 0) {
  array.forEach(item => { /* process */ });
}
```

### LaTeX in JSON
```json
{
  "answer": "$\\\\mathbf{F}_2 \\\\approx 66$ lb"
}
```

### URL Encoding Paths
```javascript
const encoded = path.split('/').map(encodeURIComponent).join('/');
```

---

## 9. Physics Problem Verification - Right-Hand Rule

### Issue
Incorrect particle identification in cyclotron motion problem due to misapplying the right-hand rule for magnetic force on charged particles.

### Critical Understanding
For magnetic force $\vec{F} = q(\vec{v} \times \vec{B})$:
- The cross product $\vec{v} \times \vec{B}$ gives the direction for **POSITIVE charge**
- For **NEGATIVE charge** (electron), force is **OPPOSITE** to the cross product direction
- This is critical for particle identification problems

### Example Error
- B field OUT of page, particle moving COUNTERCLOCKWISE
- $\vec{v} \times \vec{B}$ points OUTWARD (radially)
- For proton (+): Force outward → NOT centripetal (wrong!)
- For electron (−): Force INWARD → centripetal (correct!)

### Solution
Always:
1. Identify required force direction (usually toward center for circular motion)
2. Determine cross product direction using right-hand rule
3. If force needs to be opposite to cross product → negative charge
4. If force matches cross product → positive charge

### Cascading Corrections
When particle type is corrected:
- **Update mass** in all subsequent calculations (m_e ≠ m_p by factor ~1800)
- **Recalculate radius**: r = mv/(qB) changes dramatically
- **Recalculate period**: T = 2πm/(qB) changes significantly
- Verify ALL dependent parts of multi-part problems

### Best Practice
- Always verify physics answers against answer keys before finalizing
- Check direction carefully for vector problems
- When correcting foundational errors, systematically update ALL dependent calculations

---

## 10. Magnetic Dipole Moment Direction

### Issue
Incorrect magnetic dipole moment direction due to not carefully applying right-hand rule to current loops.

### Solution
For current loop in xz-plane:
- Curl fingers in direction of current flow (as shown in diagram)
- Thumb points in direction of $\vec{\mu}$
- Check if this is +ĵ or −ĵ direction
- **Never assume** - always verify against problem diagram

### Cascading Effects
When dipole direction is wrong:
- **Potential energy** U = −$\vec{\mu}$ · $\vec{B}$ sign flips
- **Torque** $\vec{\tau}$ = $\vec{\mu}$ × $\vec{B}$ components change sign
- Must update ALL dependent parts (b, c, d)

### Best Practice
- Draw diagram with current direction clearly marked
- Apply right-hand rule carefully
- Double-check against answer key
- Update all dependent calculations when correcting direction

---

## 11. UI Auto-Load Behavior

### Issue
Welcome screen appeared briefly but was immediately replaced by auto-loaded quiz content, defeating the purpose of the welcome screen.

### Root Cause
On page initialization, `populateSidebar()` was called with `autoLoad=true`, which automatically loaded the first quiz of the first test set.

### Solution
Change initialization to `autoLoad=false` to prevent automatic content loading:
```javascript
populateSidebar(firstSubject.testSets, false); // Don't auto-load
```

### UI State Management
When designing welcome/landing screens:
1. **Hide controls** that aren't applicable (timer, navigation, stats)
2. **Show welcome** by default
3. **User action triggers** transition: quiz selection → hide welcome, show controls
4. **Explicit state management**: Check if content exists before rendering

### Best Practice
- Never auto-load content if you want to show a welcome/landing state
- Control UI element visibility explicitly based on application state
- Test initial page load behavior separately from navigation behavior

---

## 12. Code Refactoring for Maintainability

### Issue
Duplicate code for showing Easter egg messages, making future changes harder.

### Solution
Create reusable utility functions:
```javascript
function showEasterEggMessage(messageHTML) {
  // Single implementation used by multiple functions
}
```

### Pattern
1. **Identify repeated code** (even if slightly different)
2. **Extract to function** with parameters for variations
3. **Call from multiple places** with different messages
4. **Easier to update** styling, timing, animations in one place

### Best Practice
- Apply DRY (Don't Repeat Yourself) principle
- Refactor immediately when you notice duplication
- Use parameters for variations rather than copying code
- Future changes only need to be made once

---

## 13. Testing Discipline and User Confirmation

### Issue
Changes pushed to production without local testing could cause issues.

### Solution
Always follow this workflow:
1. **Make changes** in local environment
2. **Test locally** in browser (refresh with Ctrl+F5 to clear cache)
3. **Get user confirmation** that changes work as expected
4. **Then commit and push** to repository

### Benefits
- Catch issues before they reach production
- User verifies behavior matches requirements
- Reduces rollback needs
- Builds confidence in deployment process

### Best Practice
- **Never push without testing** "Don't push/commit until changes are confirmed locally"
- Use browser dev tools to verify JavaScript behavior
- Test edge cases (welcome screen, empty states, transitions)
- Get explicit user approval before deploying

---

## 14. Section Headers in Quiz JSON - Use Markdown Headers, Not Bold

### Issue
Section labels in quiz answers using `**Label:**` pattern didn't render as bold consistently. This happened multiple times when creating quiz.json files.

### Root Cause
Bold text (`**text**`) in Markdown has inconsistent rendering when used for section headers, especially with newlines. The proper solution is to use Markdown headers (`##`) for sections instead of bold text.

### Correct Solution
Use `##` Markdown headers for section labels in the `explanation` field, and keep the `answer` field brief.

**Correct Pattern (from Test 1):**
```json
{
  "answer": "$M_D = 1{,}380\\,\\mathrm{lb\\cdot ft}$ (counterclockwise)",
  "explanation": "## Given\\n\\n$W = 100\\,\\mathrm{lb}$, with 40 lb loads at A and C.\\n\\n## Step 1: Identify the support type\\n\\nPoint D is a fixed-end support...\\n\\n## Step 2: Sum moments about D\\n\\nTaking counterclockwise moments as positive:\\n\\n$$\\\\Sigma M_D = 40(8)...$$"
}
```

### Structure
1. **answer field**: Brief, concise final answer (like "$M_D = 1{,}380\\,\\mathrm{lb\\cdot ft}$")
2. **explanation field**: Detailed solution with `##` headers for sections like "## Given", "## Step 1:", "## Step 2:", "## Summary"

### Working Examples
From Test 1:
- `## Step 1: Geometry and Distances` ✅
- `## Given` ✅
- `## Step 2: Moment of Force P About A` ✅
- `## Summary` ✅

### Non-Working Pattern
- `**Step 1:** Description...` ❌ (bold doesn't render as section header)
- `**Step 1: Identify the support type**\\nPoint D is...` ❌ (bold with newline issues)

### Best Practice
- Use `##` for main sections in the explanation field
- Use `###` for subsections if needed
- Keep answer field brief (just the final answer)
- Put all detailed work in the explanation field with proper headers
- Reference Test 1 quiz.json as the template for formatting

---

## 15. Coordinate System Orientation - Always Check the Diagram

### Issue
Assumed standard coordinate convention (z = vertical) when solving 3D statics problem, leading to completely wrong solution.

### Root Cause
Made assumption based on typical conventions rather than carefully reading the coordinate axes shown in the problem diagram. The diagram clearly showed:
- x = horizontal
- y = vertical  
- z = in/out of screen

This caused the 840 lb downward force to be incorrectly placed in the -z direction instead of the -y direction.

### Impact
- Moment equations gave impossible results (negative cable tensions)
- Spent significant time troubleshooting geometry instead of recognizing coordinate system error
- Solution was off by a factor of 2× (630 vs 1,257 lb for one cable)

### Solution
**ALWAYS** start problem solving by:
1. **Identify coordinate system** from diagram FIRST
2. **Note which axis is vertical** (don't assume it's z)
3. **Verify force directions** match the coordinate system
4. **Look for axis labels** in diagram (they're usually there!)

### Correct Approach
```
Step 1: Read diagram → x horizontal, y vertical, z depth
Step 2: 840 lb downward force → (0, -840, 0) in this system
Step 3: Set up equations with correct force vector
```

### Best Practice
- **Never assume coordinate conventions** - different textbooks/problems use different systems
- **Read the diagram carefully** before starting calculations
- **Double-check force directions** against the stated coordinate system
- **If equations give impossible results** (negative tensions, etc.), suspect coordinate system error
- **Save time** by verifying geometry first rather than troubleshooting math

### Reference
Problem #2 (3D statics with cables): Correct solution has T_BD = 1,257 lb, T_BE = 1,046 lb when using proper y-vertical coordinate system.

---

## 16. LaTeX Escaping: Answer Field vs Explanation Field

### Issue
Answer fields were showing raw LaTeX text (e.g., "mathrm" instead of rendering properly) even with correct double backslashes.

### Root Cause
Different JSON fields require different levels of escaping:
- **Answer field** (short text): Use `\\,\\mathrm` (double backslash)
- **Explanation field** (long text): Use `\\\\,\\\\mathrm` (quadruple backslash, or double-escaped)

### Solution
When LaTeX in answer field doesn't render:
1. Check if you're using quadruple backslashes (`\\\\\\\\`) - if so, reduce to double (`\\\\`)
2. For inline math in answer: `$T_{BD} = 1{,}257\\,\\mathrm{lb}$`
3. For display math in explanation: `$$T_{BD} = 1{,}257\\\\,\\\\mathrm{lb}$$`

### Pattern Recognition
- Problems 1 and 4 rendered correctly with double backslashes in answer field
- Problems 2, 3, 5, 6 failed with quadruple backslashes, fixed when changed to double

### Best Practice
- **Answer field:** Double backslashes (`\\`)
- **Explanation field:** Quadruple backslashes (`\\\\`) in display math
- When copying between fields, adjust escaping accordingly

---

## 17. Display Math Block Rendering Issues

### Issue
Complex LaTeX equations wouldn't render, appearing as raw text instead of formatted math.

### Multiple Causes Discovered

**1. Colon immediately before display math:**
```json
❌ "Taking moments about A:\n\n$$equation$$"
✅ "Taking moments about A.\n\n$$equation$$"
```

**2. Insufficient blank lines:**
- Standard: text, blank line (`\n\n`), equation
- Sometimes needed: text, **two blank lines** (`\n\n\n`), equation
- Especially after descriptive text ending with colon

**3. Overly complex equations:**
```json
❌ $$\vec{r}_{AB} \times (T_{BD}\hat{u}_{BD}) + \vec{r}_{AB} \times (T_{BE}\hat{u}_{BE}) + \vec{r}_{AC} \times \vec{F}_C = \vec{0}$$
✅ $$\sum \vec{M}_A = \vec{0}$$
```
Long equations with multiple subscripts, cross products, and unit vector hats can fail to parse.

**4. Inline math near display math:**
Avoid complex inline LaTeX (`$\vec{r}_{AB} = (6, 0, 0)$`) immediately before/after display blocks.

### Solution Strategies
1. **Remove colons** before display math - use periods instead
2. **Add extra blank line** if equation still doesn't render
3. **Simplify complex equations** - break into multiple simpler blocks or use summation notation
4. **Minimize inline math** around display blocks - use plain text when possible

### Best Practice
- Test rendering after adding each display math block
- If equation doesn't render, try simplifying before adding more blank lines
- Keep equations focused and concise

---

## 18. Problem Verification Discipline

### Issue
Multiple problems had incorrect solutions that made it into quiz.json from answer keys.

### Examples from Test 2 (A)
1. **Problem #1:** M_D = 20 ft·lb (wrong) vs -120 ft·lb (correct) - off by 6×
2. **Problem #3:** Used wrong dimensions (middle rectangle 0.5 in vs 0.25 in)
3. **Problem #5:** Multiple incorrect attempts before finding right load distribution
4. **Problem #6:** F_FE = 400 lb (wrong) vs 875 lb (correct)

### Root Cause
- Relying on provided answer keys without independent verification
- Answer keys themselves can contain errors
- Not carefully reading dimensions from problem diagrams

### Solution
**Always solve problems independently:**
1. **Read diagram carefully** - verify all dimensions, coordinates, orientations
2. **Set up from first principles** - don't assume key has correct setup
3. **Solve step-by-step** - show all work to catch errors early
4. **Verify against multiple sources** - use ChatGPT, hand calculations, etc.
5. **Check reasonableness** - do magnitudes and signs make sense?

### Verification Checklist
- [ ] Coordinate system identified from diagram
- [ ] All dimensions/loads read directly from diagram
- [ ] Force/moment equilibrium equations set up correctly
- [ ] Calculation checked with external tool (ChatGPT, calculator)
- [ ] Answer magnitude and sign are reasonable
- [ ] Units are correct

### Best Practice
**Treat answer keys as suggestions, not truth.** Always verify solutions independently before adding to quiz.json. When discrepancies arise, solve from scratch rather than trying to reconcile conflicting answers.

---

*This document should be updated whenever significant lessons are learned during development.*
