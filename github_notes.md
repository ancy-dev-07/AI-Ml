# Github

## Begining

To check the current status `git status`

```bash
PS C:\Users\ngima\Documents\GitHub\AI-Ml> git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        github_notes.md

nothing added to commit but untracked files present (use "git add" to track)
```

## Git Track (Add)

- To add the file `git add <filename>`
- To add all files `git add .`

```bash
PS C:\Users\ngima\Documents\GitHub\AI-Ml> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   github_notes.md

PS C:\Users\ngima\Documents\GitHub\AI-Ml> 
```

## Create commit message

- To add commit message `git commit -m "Initialized"`

<!-- Rest will be done by Ancy salmankhan -->

## Branch

- To create new branch `git branch ancy`
- To check available branches `git branch`

```bash
git branch
  ancy
* main
```

- To change branch `git checkout AvailableBranchName`

```bash
git checkout ancy
Switched to branch 'ancy'
PS C:\Users\ngima\Documents\GitHub\AI-Ml> git branch
* ancy
  main
PS C:\Users\ngima\Documents\GitHub\AI-Ml> 
```
