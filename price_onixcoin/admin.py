from django.contrib import admin
from .models import Yobit, PriceBtcLocalbitcoin, PriceOnix
# Register your models here.


@admin.register(Yobit)
class AdminLocalBitcoin(admin.ModelAdmin):
    list_display = ('btc_onx_buy', 'usd_btc_buy',
                    'btc_onx_sell', 'usd_btc_sell', )


@admin.register(
    PriceBtcLocalbitcoin
)
class AdminLocalBitcoin(admin.ModelAdmin):
    list_display = ('price_btc_usd_avg_1h', 'price_btc_usd_avg_6h',
                    'price_btc_usd_avg_12h', 'price_btc_usd_avg_24h',
                    'price_btc_bs_avg_1h', 'price_btc_bs_avg_6h',
                    'price_btc_bs_avg_12h', 'price_btc_bs_avg_24h',)


@admin.register(
    PriceOnix
)
class AdminLocalBitcoin(admin.ModelAdmin):
    list_display = ('btc_onx_buy', 'onx_bs_buy', 'usd_onx_buy', 'btc_onx_sell', 'onx_bs_sell', 'usd_onx_sell')
