name: spark
# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "main" branch
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  # Allows you to run this workflow manually from the Actions tab
  repository_dispatch:
    types: [spark]
# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  spark:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - run: ls -la  
