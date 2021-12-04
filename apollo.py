import arguments, diff_checker, token_checker, epsilon_checker

args = arguments.parse()

with open(args.user_output) as user_out, open(args.judge_output) as judge_out:
    print(epsilon_checker.check(user_out, judge_out, 1e-6).to_string())
