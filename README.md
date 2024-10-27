I'm trying to recreate the viral [One Million Checkboxes game](https://github.com/nolenroyalty/one-million-checkboxes) while following best practices using Python, FastAPI, and Poetry. 

Goals:
- [x] Follow [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).
- [ ] Follow [some project structure](https://github.com/zhanymkanov/fastapi-best-practices).
- [ ] Track tasks / bugs using github issues.
- [ ] Set up prototype with single user.
- [ ] Deploy a live version.
- [ ] Set up rate limiting.
- [ ] Because users of the original game have developed bots implement User Auth / anti-botting measures.
- [ ] Scale to multiple millions of checkboxes.
- [ ] Set up logging.
- [ ] Maintain consistency.
- [ ] Testing (unit/integration).
- [ ] Fault tolerance testing (chaos engineering).
- [ ] Potentially recreate everything in Go as well.
- [ ] Play around with UI development (coming from no experience)
- [ ] Implement User Leaderboard.
- [ ] Distributed Locking.
- [ ] Event broadcasting.
- [ ] Documentation.
- [ ] CI/CD.

## Code Quality

I used [Ruff](https://github.com/charliermarsh/ruff) for linting to maintain code quality and consistency.

### Running Ruff Locally

To ensure consistency with the CI workflow, run Ruff locally before committing:

```bash
poetry run ruff .
```
## Continuous Integration

I used [GitHub Actions](https://github.com/features/actions) to enforce code quality standards through automated linting with Ruff.

### Linting Workflow

The linting workflow runs Ruff on all pushes and pull requests to the `main` and `develop` branches.

#### Workflow Configuration

The workflow is defined in `.github/workflows/ruff.yml` and performs the following steps:

1. **Checks out the code.**
2. **Sets up Python.**
3. **Installs dependencies using Poetry.**
4. **Runs Ruff to lint the codebase.**

