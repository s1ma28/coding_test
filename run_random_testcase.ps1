
$total = 0
# case: �����_���e�X�g�P�[�X�Ŏ���������
while (1) {
    python ./generate_random_testcase.py > input.txt
    $in = (Get-Content input.txt)
    $out = (Get-Content input.txt | python '.\B - ���ߗ���.py')
    $total++
    Write-Host "in: ${in}"
    Write-Host "out: ${out}"
    Write-Host "try count: ${total}"
    Start-Sleep -s 3
}

# $correct = 0
# # case: �𒼉��Ɣ�r����𒼉��Ɣ�r����
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