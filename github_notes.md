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

## Merge

- To merge current branch with new branch to main branch
- Go to main branch 

```bash
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git merge ancy
Merge made by the 'ort' strategy.
 first.js                |  7 ++++++
 first.txt               |  1 +
 github_notes.md         | 28 ++++++++++++++++++++++++
 python1/Numpy/basic.py  | 58 ++++++++++++++++++++++++++++++++++++++++++++-----
 python1/Numpy/notes.txt | 14 +++++++++++-
 5 files changed, 101 insertions(+), 7 deletions(-)
 create mode 100644 first.js
 create mode 100644 first.txt
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git add .
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git commit -m ""
error: switch `m' requires a value
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git commit -m "q"
On branch main
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 425 bytes | 425.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/ancy-dev-07/AI-Ml.git
   f3b99d3..a28f58c  main -> main
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git add .        
warning: in the working copy of 'github_notes.html', LF will be replaced by CRLF the next time Git touches it
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git commit -m "q"
[main 224bedd] q
 1 file changed, 42 insertions(+), 378 deletions(-)
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git push         
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.54 KiB | 525.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/ancy-dev-07/AI-Ml.git
   a28f58c..224bedd  main -> main
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git add .        
warning: in the working copy of 'github_notes.html', LF will be replaced by CRLF the next time Git touches it
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git commit -m "q"
[main e75b88f] q
 1 file changed, 383 insertions(+), 23 deletions(-)
(env) PS C:\Users\ngima\Documents\GitHub\AI-Ml> git push         
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 2.97 KiB | 1.48 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/ancy-dev-07/AI-Ml.git
   224bedd..e75b88f  main -> main
```