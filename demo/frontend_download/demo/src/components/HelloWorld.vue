<template>
  <div>
    <button @click='downLoad'>test</button>
  </div>
</template>

<script>
import FileSaver from 'file-saver'

export default {
  methods: {

    downLoad () {
      const data = [
        {
          city: '邵阳市',
          index: 13,
          industry: '金属表面处理及热处理加工',
          parent_company: '',
          company_name: '邵东县和天电镀中心有限公司',
          advice: '50%'
        },
        {
          city: '永州市',
          index: 5,
          industry: '',
          parent_company: '',
          company_name: '永州市北控污水净化有限公司（新田县分公司）',
          advice: '50%'
        },
        {
          city: '娄底市',
          index: 2,
          industry: '',
          parent_company: '',
          company_name: '湘村高科农业股份有限公司湘村黑猪原种场',
          advice: '50%'
        }
      ]
      const fileName = 'test.csv'
      const { Parser } = require('json2csv')
      const fields = [
        {
          label: '序号',
          value: 'index'
        },
        {
          label: '地区',
          value: 'city'
        },
        {
          label: '行业',
          value: 'industry'
        },
        {
          label: '所属上市公司',
          value: 'parent_company'
        },
        {
          label: '公司名称',
          value: 'company_name'
        },
        {
          label: '建议减按征收比例',
          value: 'advice'
        }
      ]
      const opts = {
        fields
      }
      const json2csvParser = new Parser(opts)
      const csv = json2csvParser.parse(data)
      let blob = new Blob(['\uFEFF' + csv], {
        type: 'text/plaincharset=utf-8'
      })
      FileSaver.saveAs(blob, fileName)
    }
  }
}
</script>

<style scoped>
</style>
