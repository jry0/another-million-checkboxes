# Overview
One million shared and editable RBG pixels utilizing my [personal key-value store](https://github.com/jry0/personal-kv-store).

Inspired by the viral [One Million Checkboxes game](https://github.com/nolenroyalty/one-million-checkboxes) and [r/place](https://en.wikipedia.org/wiki/R/place). 
Made with Python / FastAPI. Also, the classic [million-dollar-billboard](http://www.milliondollarhomepage.com/).



## Goals:
- Create simple backend using Redis as datastore, and test endpoints.
- Create simple frontend to test user interactability.
- Replace data store with [personal-kv-store](https://github.com/jry0/personal-kv-store).
- Follow [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).
- Follow [some project structure](https://github.com/zhanymkanov/fastapi-best-practices).
- Track tasks / bugs using github issues.
- Deploy a live version.
- Set up rate limiting.
- Scale to multiple millions of pixels.
- Set up logging.
- Testing (unit/integration).
- Potentially recreate everything in Go as well.
- Play around with UI development (coming from little experience), re-implement using React.
- Feat: Implement a User Leaderboard.
- CI/CD.

## Code Quality

I used [Ruff](https://github.com/charliermarsh/ruff) for linting / formatting and [pre-commit](https://pre-commit.com/) git hooks for code consistency. 

## Ruff CI
For fun, I've also added a simple [Ruff CI workflow](https://github.com/jry0/shared-pixel-canvas/blob/main/.github/workflows/ruff.yml) for linting using GitHub Actions.

The workflow runs ruff on all pushes and pull requests to the `main` and `develop` branches. It performs the following steps:

1. **Checks out the code.**
2. **Sets up Python.**
3. **Installs dependencies using Poetry.**
4. **Runs Ruff to lint the codebase.**






