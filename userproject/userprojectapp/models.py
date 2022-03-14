from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)


class UserDatas(AbstractBaseUser):
    usernameAccount = models.CharField(
        max_length=100,
        null=False,
        unique=True,)
    emailAccount = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    isActive = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    walletAddress = models.CharField(max_length=100,null=False)
    evaluation = models.CharField(max_length=100,null=False)

    # def __str__(self):
    #     return self.usernameAccount

    class Meta:
        db_table = 'user_datas'

class TransferLogs(models.Model):
    userData = models.ForeignKey(UserDatas, on_delete = models.CASCADE)
    fromAddress = models.CharField(max_length=100,null=False)
    toAddress = models.CharField(max_length=100,null=False)
    amount = models.DecimalField(max_digits=4, decimal_places=4,null=False)
    token = models.CharField(max_length=100,null=False)
    time = models.DateTimeField(null=False)


    # def __str__(self):
    #     return self.projectId

    class Meta:
        db_table = 'transfer_logs'

class FundingProjects(models.Model):    
    nftId = models.PositiveIntegerField(null=False)
    startTime = models.DateTimeField(null=False)
    endTime = models.DateTimeField(null=False)
    token = models.CharField(max_length=100,null=False)
    buyPrice = models.DecimalField(max_digits=4, decimal_places=4,null=False)
    sellPrice = models.DecimalField(max_digits=4, decimal_places=4,null=False)
    gasPrice = models.DecimalField(max_digits=4, decimal_places=4,null=False)
    fundraiser = models.CharField(max_length=100,null=False)
    userLikeList = models.ManyToManyField(UserDatas,through='LikeLists',related_name='userLike')
    userFundingShare = models.ManyToManyField(UserDatas,through='FundingShares',related_name='userFunding')

    # def __str__(self):
    #     return 'nft: {} token: {} '.format(
    #         self.nftId, self.token
    #     )

    class Meta:
        db_table = 'funding_projects'

class LikeLists(models.Model):
    userData = models.ForeignKey(UserDatas, on_delete=models.CASCADE)
    fundingProject = models.ForeignKey(FundingProjects, on_delete=models.CASCADE)
    likeOrNot = models.BooleanField(blank=True)

    # def __str__(self):
    #     return f'{self.userData} {self.fundingProject} like{self.likeOrNot}'
        
    class Meta:
        db_table = 'like_lists'

class FundingShares(models.Model):
    userData = models.ForeignKey(UserDatas, on_delete=models.CASCADE)
    fundingProject = models.ForeignKey(FundingProjects, on_delete=models.CASCADE)
    share = models.DecimalField(max_digits=4, decimal_places=4,null=False)

    # def __str__(self):
    #     return f'{self.userData} {self.fundingProject} share:{self.share}'
        
    class Meta:
        db_table = 'funding_shares'

