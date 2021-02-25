
$total = 0
# case: ランダムテストケースで試し続ける
while (1) {
    python ./generate_random_testcase.py > input.txt
    $in = (Get-Content input.txt)
    $out = (Get-Content input.txt | python '.\B - 埋め立て.py')
    $total++
    Write-Host "in: ${in}"
    Write-Host "out: ${out}"
    Write-Host "try count: ${total}"
    Start-Sleep -s 3
}

# $correct = 0
# # case: 愚直解と比較する愚直解と比較する
# while (1) {
#     python ./generate_random_testcase.py > input.txt
#     $ans1 = (Get-Content input.txt | python test.py)
#     $ans2 = (Get-Content input.txt | python ./guchoku.py)
#     $total++
#     if ($ans1 -ne $ans2) {
#         Write-Host "Wrong Answer"
#         Write-Host "mytry: ${ans1}"
#         Write-Host "gucho: ${ans2}"
#         exit
#     }
#     else {
#         $correct++
#         # Write-Host "Correct"
#         Write-Host "correct ${correct} / ${total}"
#     }
# }