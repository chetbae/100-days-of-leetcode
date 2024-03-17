class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create hashmap to map emails to account index
        emailMap = {}

        # search through all accounts
        for i, account in enumerate(accounts):

            # search through all emails, starting with index 1
            for email in account[1:]:

                # if email exists in some other account, append account number to array
                if email in emailMap:
                    emailMap[email].append(i)
                
                # otherwise create new key-value
                else:
                    emailMap[email] = [i]
        
        # visit all accounts and dfs through emails that belong through the same person

        # keep track of visited accounts, visited[i] = accounts[i] is visited
        visited = [False] * len(accounts)

        # output array with merged accounts
        ans = []

        # search all accounts
        for i, account in enumerate(accounts):

            # skip if account has already been visited in dfs
            if visited[i]:
                continue
            
            # get name and emails to search through
            name, stack = account[0], account[1:]

            # make array for all associated emails
            emails = set()

            # mark account as visited
            visited[i] = True

            # dfs until no more emails
            while stack:
                current = stack.pop()
                
                # skip if current email has been visited
                if current in emails:
                    continue
                
                # add current to set
                emails.add(current)

                # find associated accounts from emailMap
                for account_i in emailMap[current]:

                    # get account, get emails
                    associatedAccount = accounts[account_i]
                    associatedEmails = associatedAccount[1:]
                    stack.extend(associatedEmails)

                    # mark account as visited
                    visited[account_i] = True

            # add merged account to answer
            ans.append([name] + sorted(emails))

        return ans