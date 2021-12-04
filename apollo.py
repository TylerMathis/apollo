import arguments, diff_checker, token_checker

args = arguments.parse()

with open(args.user_output) as user_out, open(args.judge_output) as judge_out:
    print(token_checker.check(user_out, judge_out).to_string())
