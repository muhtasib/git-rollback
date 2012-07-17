git-rollback(1) -- Undo a local or remote commit
================================

## SYNOPSIS

`git rollback` [&lt;local&gt; [-k | --keep][-w | --wipe] | &lt;remote&gt; [branch_name]]

## DESCRIPTION

Undo a commit locally or remotely.

## OPTIONS

local

Specifies the commit to undo is local.

-k | --keep

Keep the changes undone staged if you undo a commit locally. Default, changes are unstaged.

-w | --wipe

Do not keep the changes at all.

remote

Specified the commit to undo is remote.

branch_name

If undoing remotely, the branch you want to undo from. Default branch is master.

## EXAMPLES

    $ git rollback local 
    You are rolling back your local commit.
    Unstaged changes after reset:
    M	 README.md

    $ git rollback local -k
    You are rolling back your local commit.
    
    $ git rollback local -w
    You are rolling back your local commit.
    HEAD is now at 4f36a0a 2

    $ git rollback remote
     Is the branch you are currently on the same and up-to-date with the branch 'master' you want to undo the commit from? (y/n) y
     You are rolling back your remote & local commit. You want to roll back to:
     99e8e8c08841eb5bc427ab7ce57b0e7600f1ed33
     Total 0 (delta 0), reused 0 (delta 0)
     To git@github.com:sampleAuthor/Test.git
     + 28cd9f1...99e8e8c 99e8e8c08841eb5bc427ab7ce57b0e7600f1ed33 -> master (forced update)
     Unstaged changes after reset:
     M	 README.md

    $ git rollback remote documentation_branch
    Is the branch you are currently on the same and up-to-date with the branch 'documentation_branch' you want to undo the commit from? (y/n) y
    You are rolling back your remote & local commit. You want to roll back to:
    99e8e8c08841eb5bc427ab7ce57b0e7600f1ed33
    Total 0 (delta 0), reused 0 (delta 0)
    To git@github.com:sampleAuthor/Test.git
    + 28cd9f1...99e8e8c 99e8e8c08841eb5bc427ab7ce57b0e7600f1ed33 -> documentation_branch (forced update)
    Unstaged changes after reset:
    M	 README.md

## AUTHOR

Written by Leila Muhtasib &lt;<muhtasib@gmail.com>&gt;

## REPORTING BUGS

&lt;<http://github.com/muhtasib/git-rollback/issues>&gt;

## SEE ALSO

&lt;<http://github.com/muhtasib/git-rollback>&gt;
