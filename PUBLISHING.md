# Publish this folder to GitHub

No remote GitHub repository has been created as part of this artifact. The following instructions publish these **local files** after you create an empty GitHub repo called `computational-preservation`. Do **not** initialize the remote with a generated README because the local folder already contains one.

PowerShell (Windows):

```powershell
Expand-Archive .\computational-preservation.zip -DestinationPath .
cd .\computational-preservation
python -m unittest discover -s tests -v
git init -b main
git add .
git commit -m "Initial research archive: computational preservation"
git remote add origin https://github.com/datasci3nce/computational-preservation.git
git push -u origin main
```

The remote example targets `datasci3nce` as requested. First create an **empty** public repository in that account and authenticate through GitHub's supported login/credential flow. As an alternative to manual creation, after `git commit` and authentication with GitHub CLI, `gh repo create datasci3nce/computational-preservation --public --source . --remote origin --push` can create and push it; do not run both remote-creation methods. Verify the live URL and README after pushing. Avoid posting access tokens in chat or committing experiment credentials. If the remote already has commits, reconcile them rather than force-pushing.

## Before making it public

- Choose a license; **none is included yet**.
- Confirm author and independent-researcher affiliation in `paper/nca_fold_case_study/main.tex` and the compiled PDF.
- Decide whether historical evidence documents should remain public unchanged.
- Add only original experiment archives you have permission to redistribute, respecting checkpoint licenses and dataset privacy.
- Recover missing raw data and figures only from verified archives; never regenerate an empirical plot from rounded prose numbers.
- Verify the CI checks before publishing scientific claims.
