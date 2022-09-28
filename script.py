
import argparse
# import requests
# import base64
# import json
import time
from github import Github
from github import InputGitAuthor
def push_to_repo_branch_github(token,gitFileName):

    g = Github(token)
    repo = g.get_user().get_repo("apps-demo-applicationset")
    branch = "main"
    commit_user = "useradmin"
    commiter_email = "useradmin@local"
    message = "update sesuatu"
    commit_message = f"[{commit_user}] {message}"
    file = repo.get_contents(gitFileName, ref=branch)
    with open(gitFileName, 'r') as data:
        content = data.read()

    committer = InputGitAuthor(
        commit_user,
        commiter_email
    )
    check = False
    time.sleep(5)
    while not check:
        try:
            repo.update_file(
                file.path, 
                commit_message, 
                content, 
                file.sha, 
                branch=branch,
                committer=committer
            )
            check = True
            print(gitFileName + ' UPDATED')
        except Exception as e:
            print(e)
    # message = "test message"
    
    # organization = "igstbagusdharmaputra"
    # reponame = "apps-demo-applicationset"
    # path = "https://api.github.com/repos/%s/%s/contents/%s?ref=%s" % (organization,reponame,gitFileName,branch)
    # headers = {
    #     "content-type": "application/json",
    #     'Accept' : 'application/vnd.github+json',
    #     'Authorization': 'Bearer' + token
    # }
    
    # r = requests.get(path, headers=headers)
    # if not r.ok:
    #     print("Error when retrieving commit tree from %s" % path)
    #     print("Reason: %s [%d]" % (r.text, r.status_code))
    #     raise Exception
    
    # rjson = r.json()
    
    # sha = rjson['sha']
    
    # with open(gitFileName) as data:
    #     string = base64.b64encode(bytes(data.read(), 'utf-8'))
    #     content = string.decode("utf-8")

    # inputdata = {}
    # inputdata["message"]=message
    # inputdata["committer"]={'name':'admin','email':'dharmatkjone@gmail.com'}
    # inputdata["content"]=content
    # inputdata["sha"]=sha
    # inputdata["branch"]=branch

    # updateURL=f"https://api.github.com/repos/{organization}/{reponame}/contents/{gitFileName}"
    # try:
    #     rPut = requests.post(updateURL, headers=headers, data = json.dumps(inputdata))
    #     print(rPut)
    # except requests.exceptions.RequestException as e:
    #     print('Something went wrong!')
    #     print(rPut)
    #     print(rPut.headers)
    #     print(rPut.text)
    #     print(e)
        
    
    
def push_to_repo_branch_gitlab(token):
    pass
def main():
    parser = argparse.ArgumentParser(description='Git Push Repo')
    parser.add_argument(
        '--type', required=True,choices=['github', 'gitlab'], help='only github and gitlab')
    parser.add_argument(
        '--token', required=True, type=str, help='token git')
    parser.add_argument(
        '--file', required=True, type=str, help='file path')
    args = parser.parse_args()


    if args.type == "github":
        push_to_repo_branch_github(args.token,args.file)
    elif args.type == "gitlab":
        push_to_repo_branch_gitlab(args.token,args.file)

if __name__ == "__main__":
    main()