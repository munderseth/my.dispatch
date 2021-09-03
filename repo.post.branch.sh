
URL1="https://api.github.com/repos/munderseth/my.dispatch"
BRANCH="the.branch"

echo Toggle Branch via PATCH 
# Set branch "the.branch" to default
curl -X PATCH $URL1 \
-H 'Content-Type: application/json' \
-H 'Accept: application/vnd.github.v3+json' \
-H "Authorization: token $GH_TOKEN" \
-d '{
     "default_branch": "the.branch"
    }'

SEC=0
echo "Wait for $SEC secs for branch to switch"
sleep $SEC
echo Done with Sleep

echo "Post Repo Dispatch"
# Post Repository Dispatch
URL2="https://api.github.com/repos/munderseth/my.dispatch/dispatches"
curl -X POST $URL2 \
-H 'Content-Type: application/json' \
-H 'Accept: application/vnd.github.v3+json' \
-H "Authorization: token $GH_TOKEN" \
-d '{
     "event_type":"test"
    }'

SEC=3
echo "Wait for $SEC secs for branch to switch"
sleep $SEC
echo Done with Sleep

# Set "master" back to default
curl -X PATCH $URL1 \
-H 'Content-Type: application/json' \
-H 'Accept: application/vnd.github.v3+json' \
-H "Authorization: token $GH_TOKEN" \
-d '{
     "default_branch": "master"
    }'
