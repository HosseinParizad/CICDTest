# Claude Project Specification – Simple CI/CD Demo with Auto Feedback

## 🧩 Project Overview

This repository demonstrates a minimal **Node.js CI/CD pipeline** using **GitHub Actions** and **Claude Code**.  
The goal is to automatically run unit tests on every pull request and have Claude analyze and suggest fixes when tests fail.

---

## 📁 Repository Structure

```

my-ci-demo/
├── main.js
├── test/
│   └── add.test.js
├── package.json
└── .github/
└── workflows/
└── ci.yml

```

---

## ⚙️ CI/CD Behavior

1. Workflow triggers on each `push` or `pull_request` to `main`.
2. Node.js environment (v18) is set up.
3. Dependencies are installed via `npm ci`.
4. Unit tests are executed with `npm test`.
5. If all tests pass → PR can be merged.
6. If tests fail → a GitHub comment mentioning `@Claude` is automatically posted with full test logs.

---

## 🧪 Unit Testing

- Framework: **Jest**
- Command: `npm test`
- Test files: Located in `test/*.test.js`
- Success criterion: All tests must pass (exit code 0)

Expected successful output:

```

PASS  test/add.test.js
✓ adds 2 + 2 equals 4

```

---

## 🚨 Failure Handling

If any test fails:

- The GitHub Action posts a comment in the pull request:

```

@Claude Unit tests failed. Please analyze and suggest a fix: <full test output>

```

- Claude Code analyzes the logs and replies with:
- Root cause summary
- File and line location of the error
- Suggested corrected code block

Example expected Claude response:

```

The function in main.js returned incorrect result.
Replace:
return a - b;
With:
return a + b;

```

---

## 🧠 Claude Code Behavior

When triggered by `@Claude`:

1. Read the failure log included in the PR comment.
2. Identify which test(s) failed and why.
3. Propose a minimal code patch to fix the issue.
4. Respond with a clear explanation and corrected snippet.
5. (Optional future feature) Commit the fix automatically and rerun the tests.

If all tests pass, Claude should respond:

```

✅ All tests passed. Merge approved.

```

---

## 🔐 Merge Policy

- The CI workflow (`CI - Unit Tests with Claude Feedback`) must pass before merging to `main`.
- A **branch protection rule** enforces that no PR can be merged with failing checks.
- Failed tests → failed status → merge automatically blocked.

---

## 🧱 Claude Verification Tasks

When mentioned manually in a comment:

```markdown
@Claude Please verify that the CI/CD pipeline correctly blocks merges on test failures and posts feedback on PRs.
```

Claude should:

- Check `.github/workflows/ci.yml` for correctness.
- Verify triggers for `push` and `pull_request`.
- Confirm that failure logs are correctly posted.
- Suggest improvements (e.g., caching, dependency steps, coverage reports).

---

## 🚀 Future Extensions

- Claude auto-commit for trivial fixes.
- Add code coverage thresholds (e.g., 80%).
- Integration with deployment platforms (Netlify, Vercel).
- Multi-environment parallel testing.

---

_Version 1.0 – November 2025_
_Author: Hossein Parizad_

```

```
