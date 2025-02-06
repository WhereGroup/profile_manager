# Profile Manager for QGIS
A QGIS plugin for managing your profiles and data source connections.

https://plugins.qgis.org/plugins/profile_manager/

<a href="https://github.com/WhereGroup/profile_manager/assets/7661092/a64ea854-bff3-48a0-b1ff-83f3d4eaa5b7"><img src="https://github.com/WhereGroup/profile_manager/assets/7661092/a64ea854-bff3-48a0-b1ff-83f3d4eaa5b7" width="200"></a>
<a href="https://github.com/WhereGroup/profile_manager/assets/7661092/711faa86-c36c-40bc-92ab-7b73016996ae"><img src="https://github.com/WhereGroup/profile_manager/assets/7661092/711faa86-c36c-40bc-92ab-7b73016996ae" width="200"></a>
<a href="https://github.com/WhereGroup/profile_manager/assets/7661092/0c646930-88d8-45fe-81c8-4a5bf4501152"><img src="https://github.com/WhereGroup/profile_manager/assets/7661092/0c646930-88d8-45fe-81c8-4a5bf4501152" width="200"></a>
<a href="https://github.com/WhereGroup/profile_manager/assets/7661092/079665d6-e0ff-45fb-a65c-3b49cd9229de"><img src="https://github.com/WhereGroup/profile_manager/assets/7661092/079665d6-e0ff-45fb-a65c-3b49cd9229de" width="200"></a>

## Handle with care
This plugin is still in an early stage. There is no thorough, automated testing yet.
Please consider everything potentially broken and make sure you thoroughly check the
results of your actions. We welcome bug reports and ideas for improvement. Your
collaboration in coding or documenting its features and limitations would be highly
appreciated.

## Features
- Create a new profile
- Removing profiles
- Copying profiles
- Renaming profiles
- Importing data source connections from one profile to another
- Removing data source connections from a profile
- Importing (spatial) bookmarks
- Importing (data source) favourites
- Importing plugins
- Importing expressions
- Importing models
- Importing scripts
- Importing some symbology types & label settings
- Importing QGIS UI settings (e.g. hidden toolbar items)
- Exporting a profile in QGIS Deployment Toolkit (QDT) format

On all removal operations the user is being asked if they are certain
that he wants to delete given source/profile.
Additionally, before every import or deletion, a backup of the affected
profile is created in the user's home directory.

## Known (current) limitations
- Not all data source connections might be recognized and imported/removed
- Not all data source connection types are supported
- Python expression functions are not supported
- Not all style things are supported, e.g. not 3D symbols, color ramps,
  tags, etc.
- Errors might not always be communicated clearly so please TEST your
  migrated configurations before discarding originals!
- Creating a new profile does not lead to the same result as creating
  a new profile in the QGIS GUI, e.g. the QGIS3.ini is not populated
  with defaults.

## Funding development
If you consider this plugin useful and would like to see it improved, e.g.
with support for more profile settings, becoming more stable, being more
thoroughly documented, leave the "experimental" plugin status or whatever
you desire, you can fund development. Contact us at info@wheregroup.com
