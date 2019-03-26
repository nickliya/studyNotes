
<template>
    <view class="content">
        <calendar 
        :selected="selected" 
        :lunar="true" 
        :disable-before="true" 
        :start-date="'2019-1-2'"
        :end-date="'2019-2-20'"
        @getdate="getdate" />

    </view>
</template>

<script>
import calendar from '../../components/mehaotian-calendar/mehaotian-calendar.vue';
export default {
    components: {
        calendar
    },
    data() {
        return {
            selected: [
                {
                    date: '2018-12-26'
                },
                {
                    date: '2018-12-27'
                },
                {
                    date: '2018-12-28'
                },
                {
                    date: '2019-1-29'
                }
            ]
        };
    },
    methods: {
        getdate(e) {
            console.log(e);
        }
    }
};
</script>