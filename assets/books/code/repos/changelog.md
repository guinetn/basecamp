# Changelog

A changelog is a file which contains a curated, chronologically ordered list of notable changes for each version of a project.

***Why keep a changelog?***
To make it easier for users and contributors to see precisely what notable changes have been made between each release (or version) of the project.

***Who needs a changelog?***
People do. Whether consumers or developers, the end users of software are human beings who care about what's in the software. When the software changes, people want to know why and how.


## GUIDING PRINCIPLES
- Changelogs are for humans, not machines.
- There should be an entry for every single version.
- The same types of changes should be grouped.
- Versions and sections should be linkable.
- The latest version comes first.
- The release date of each version is displayed.
- Mention whether you follow Semantic Versioning.

## TYPES OF CHANGES
 
- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

## Tips

Keep an Unreleased section at the top to track upcoming changes.

This serves two purposes:
- People can see what changes they might expect in upcoming releases
- At release time, you can move the Unreleased section changes into a new release version section.


## A good change log sticks to these principles:

It’s made for humans, not machines, so legibility is crucial.
Easy to link to any section (hence Markdown over plain text).
One sub-section per version.
List releases in reverse-chronological order (newest on top).
Write all dates in YYYY-MM-DD format. (Example: 2012-06-02 for June 2nd, 2012.) It’s international, sensible, and language-independent.
Explicitly mention whether the project follows Semantic Versioning.
Each version should:
List its release date in the above format.
Group changes to describe their impact on the project, as follows:
    Add for new features.
    Change for changes in existing functionality.
    Deprecated for once-stable features removed in upcoming releases.
    Remove for deprecated features removed in this release.
    Fix for any bug fixes.
    Security to invite users to upgrade in case of vulnerabilities.

    Always have an "Unreleased" section at the top for keeping track of any changes.
        people can see what changes they might expect in upcoming releases
        At release time, you just have to change "Unreleased" to the version number and add a new "Unreleased" header at the top.

### More
- https://keepachangelog.com/en/1.0.0/




```md
# changelog 'git log diff'  (journal des modifications) 

# November 6, 2017
# We integrated TaxJar for automated sale tax calculation, especially VAT. Details.
# You can now pause and resume a subscription from the dashboard. Details.
# We added the documentation for our subscriptions API . Details.

# October 3, 2017
# Subscriptions & recurring plans went through a complete refactoring. Many improvements now live. Details.
# Snipcart.api.plans is now obsolete, you should update your code to use Snipcart.api.items instead. Details.
# Subscription webhooks have been updated, please take a look at the changes. Details.

# September 11, 2017
...

# Don’t let your friends dump git logs into changelogs.

# A change log is a file which contains a curated (organised), chronologically ordered list of notable changes for each version of a project.
# Easier for users and contributors to see changes made between each release (or version) of the project
# Log diffs are full of noise — by nature
```
