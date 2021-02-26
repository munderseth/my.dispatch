
URL1="https://api.github.com/repos/munderseth/my.dispatch"

# Set branch "the.branch" to default
curl -X PATCH $URL1 \
-H 'Content-Type: application/json' \
-H 'Accept: application/vnd.github.v3+json' \
-H "Authorization: token $GH_TOKEN" \
-d '{
     "default_branch": "the.branch"
    }'

# Post Repository Dispatch
URL2="https://api.github.com/repos/munderseth/my.dispatch/dispatches"
curl -X POST $URL2 \
-H 'Content-Type: application/json' \
-H 'Accept: application/vnd.github.v3+json' \
-H "Authorization: token $GH_TOKEN" \
-d '{
     "event_type":"test"
    }'

# Sleep until ?
echo Sleep ..
sleep 10
echo Done with Sleep

# Set "master" back to default
curl -X PATCH $URL1 \
-H 'Content-Type: application/json' \
-H 'Accept: application/vnd.github.v3+json' \
-H "Authorization: token $GH_TOKEN" \
-d '{
     "default_branch": "master"
    }'
