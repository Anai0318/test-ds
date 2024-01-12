from django.db import models



class Scrape(models.Model):
    
    # 加害者のデータ
    
    offender_age_number_0_9 = models.IntegerField('加害者(0歳〜9歳)')
    
    offender_age_number_10_19 =  models.IntegerField('加害者(10歳〜19歳)')
    
    offender_age_number_20_29 = models.IntegerField('加害者(20歳〜29歳)')
    
    offender_age_number_30_39 = models.IntegerField('加害者(30歳〜39歳)')
    
    offender_age_number_40_49 = models.IntegerField('加害者(40歳〜49歳)')
    
    offender_age_number_50_59 = models.IntegerField('加害者(50歳〜59歳)')
    
    offender_age_number_60_69 = models.IntegerField('加害者(60歳〜69歳)')
    
    offender_age_number_70_79 = models.IntegerField('加害者(70歳〜79歳)')
    
    offender_age_number_80_89 = models.IntegerField('加害者(80歳〜89歳)')
    
    offender_age_90_older = models.IntegerField('加害者(90歳~)')
    
    unknown = models.IntegerField('年齢不明')
    
    offender_sum_total = models.IntegerField('加害者の全世代の総数')


    # 被害者のデータ
    
    victim_age_number_10_19 = models.IntegerField('加害者(10歳~19歳)')
    
    victim_age_number_20_29 = models.IntegerField('加害者(20歳~29歳)')
     
    victim_age_number_30_39 = models.IntegerField('加害者(30歳~39歳)')
      
    victim_age_number_40_49 = models.IntegerField('加害者(40歳~49歳)')
    
    victim_age_number_50_59 = models.IntegerField('加害者(50歳~59歳)')

    victim_sum_total = models.IntegerField('被害者の全世代の総数')
    
    # 犯行に用いた武器等（素手も含む）
    
    personal_weapons = models.IntegerField('身体を使った攻撃(手、足など)')
    
    handgun = models.IntegerField('ハンドガン')
    
    knife_cutting_instrument = models.IntegerField('鋭利な凶器')
    
    firearm = models.IntegerField('火器')
    
    none = models.IntegerField('none')
    
    type_of_weapons_sum_total = models.IntegerField('反抗に用いた武器の総数')
    