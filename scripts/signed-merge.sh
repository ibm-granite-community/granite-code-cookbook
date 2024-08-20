#!/usr/bin/env zsh

script=$(basename $0)

help() {
	cat <<EOF
Perform a merge that signs ALL commits, which the public GitHub GUI does NOT do
when doing a PR merge.

Usage: $script [-h|--help] [-n|--noop] [-t|--target branch] source_branch
Where the optional arguments are the following:
  -h | --help              Print this message and quit.
  -n | --noop              Print commands, but don't execute them.
  -t | --target branch     Merge to this target branch. Default: current branch
  -p | --pr PR             Pull request number. See note below.
  --no-push                Don't push the merge upstream. Default: merge is pushed upstream.

Where the required argument is the following:
  source_branch            Merge from this source branch.

This script is required for PR merges, because the GitHub public UI doesn't offer
the ability to sign merge commits, causing DCO check failures. This script works 
around this problem, although it can be used for any merges.

To perform PRs, use the GitHub UI to create it as you would normally. DO NOT PERFORM
THE MERGE WITH THE UI. Instead, note the PR number, e.g., "20", then run this script 
locally, specifying the correct target (default is the current branch) and source
branches and use the "--pr PR" command to specify the PR number. This option will also
change the merge commit message from the default:
  Merge from <source_branch> to <target_branch> with signoff.
to
  Manual merge of PR #<pr_num> from <source_branch> to <target_branch> with signoff.
EOF
}

error() {
	echo "ERROR: $@"
	echo
	help
	exit 1
}

target_branch=$(git br --show-current)
source_branch=
pr_num=
message_header="Merge"
: ${NOOP:=}
let no_push=1
while [[ $# -gt 0 ]]
do
	case $1 in 
		-h|--help)
			help
			exit 0
			;;
		-n|--noop)
			NOOP=echo
			;;
		-p|--pr)
			shift
			pr_num=$1
			message_header="Manual merge of PR #$pr_num"
			;;
		-t|--target)
			shift
			target_branch=$1
			;;
		--no-push)
			let no_push=0
			;;
		-*)
			error "Unrecognized argument $1"
			;;
		*)
			[[ -z "$source_branch" ]] || error "Too many 'source' branch arguments."
			source_branch=$1
			;;
	esac
	shift
done

[[ -n "$source_branch" ]] || error "Must specify a source branch."

echo "Target branch: $target_branch"
echo "Source branch: $source_branch"
echo "Don't push?    $([[ $no_push -eq 0 ]] && echo yes || echo no)"
echo "Don't execute: $([[ -n "$NOOP" ]]   && echo yes || echo no)"
echo

# Step 1: Update the repository with the latest changes on both branches. Sign any updates!
# Note that we finish on the target branch

$NOOP git checkout $source_branch
$NOOP git pull --signoff

$NOOP git checkout $target_branch
$NOOP git pull --signoff

# Step 2: Merge the source branch into the target branch, **without committing**.
# Note that git merge does not have a --signoff flag, unfortunately, which is why 
# we have to do it this way.

$NOOP git merge --no-commit $source_branch

# Step 3: Commit the changes with signoff.

$NOOP git commit --signoff -m "$message_header from $source_branch to $target_branch with signoff."

# Step 4: Push the changes upstream.

[[ $no_push -eq 0 ]] || $NOOP git push -u origin $target_branch