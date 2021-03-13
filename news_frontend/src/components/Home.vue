<template>
  <div class="home">
    <el-row display="margin-top:10px" style="margin-top: 10px">
      <el-form :model="inputForm" :rules="rules" ref="inputForm" class="demo-inputForm">
        <el-col :span="4">
          <el-form-item prop="name">
            <el-input v-model="inputForm.name" placeholder="请输入新闻分类名称"></el-input>
          </el-form-item>
        </el-col>
      </el-form>
      <el-button type="primary" icon="el-icon-edit" @click="addNewsCategory('inputForm')"
                 style="float:left; margin: 2px;">新增
      </el-button>
    </el-row>
    <el-row style="margin-top: 10px">
      <el-table :data="dataList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" align="center">
          <template scope="scope"> {{ scope.row.id }}</template>
        </el-table-column>
        <el-table-column prop="name" label="分类名称" align="center">
          <template scope="scope"> {{ scope.row.name }}</template>
        </el-table-column>
        <el-table-column prop="created_time" label="添加时间" align="center">
          <template scope="scope"> {{ scope.row.created_time|datefilter}}</template>
        </el-table-column>
        <el-table-column label="操作" align="center">
          <template slot-scope="scope">
            <el-button size="mini" type="info" icon="el-icon-chat-dot-round" @click="readNewsCategory(scope)">查看
            </el-button>
            <el-button size="mini" type="primary" icon="el-icon-edit-outline" @click="editNewsCategory(scope)">编辑
            </el-button>
            <el-button size="mini" type="danger" icon="el-icon-delete" @click="delNewsCategory(scope)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    <el-dialog title="查看结果" :visible.sync="dialogReadVisible">
      <el-form :model="readData">
        <el-form-item label="分类名称">
          <el-input auto-complete="off" v-model="readData.name"></el-input>
        </el-form-item>
      </el-form>
    </el-dialog>
    <el-dialog title="修改名称" :visible.sync="dialogUpdateVisible" @close="closeDialog('updateData')">
      <el-form :model="updateData" :rules="rules" ref="updateData" class="demo-updateData">
        <el-form-item label="分类名称" prop="name">
          <el-input auto-complete="off" v-model="updateData.name"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="handleCancel('updateData')">取 消</el-button>
        <el-button type="primary" @click="handleConfirm('updateData')">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import moment from 'moment'

  export default {
    name: "Home",
    // 时间格式过滤器
    filters: {
      datefilter: function (value) {
        return moment(value).format('YYYY-MM-DD HH:mm:ss');
      }
    },
    //数据展示
    data() {
      return {
        dataList: [],
        dialogReadVisible: false,
        dialogUpdateVisible: false,
        readData: {},
        oldData: {},
        updateData: {name: ''},
        inputForm: {name: ''},
        rules: {
          name: [{required: true, message: '请输入新闻分类名称', trigger: 'blur'},]
        }
      }
    },
    //html加载完成后执行
    created: function () {
      this.showNewsCategory()
    },
    // ajax请求api
    methods: {
      addNewsCategory(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$axios.post('/news_category/', {"name": this.inputForm.name})
              .then(response => {
                console.log(response.data);
                if (response.status === 201 & response.data["id"] != null) {
                  this.$message.success('新增新闻分类成功');
                  this.showNewsCategory();
                  this.ruleForm.name = ''
                } else {
                  this.$message.error('新增新闻分类失败，请重试');
                  this.showNewsCategory();
                  this.ruleForm.name = ''
                }
              })
              .catch(function (error) {
                console.log(error);
              })
          } else {

          }
        })
      },
      showNewsCategory() {
        this.$axios.get('/news_category/')
          .then(response => {
            console.log(response.data);
            if (response.status === 200 & response.data["count"] > 0) {
              this.$message.success('查询数据成功');
              this.dataList = response.data['results']
            } else {
              this.$message.error('查询数据失败')
            }
          }).catch(function (error) {
          console.log(error);
        });
      },
      readNewsCategory(scope) {
        this.dialogReadVisible = true;
        this.readData.name = scope.row.name

      },
      editNewsCategory(scope) {
        this.dialogUpdateVisible = true;
        this.updateData = Object.assign({}, {
          id: scope.row.id,
          name: scope.row.name,
        });
        this.oldData = Object.assign({}, {
          id: scope.row.id,
          name: scope.row.name,
        })
      },
      closeDialog(formName) {
        this.$refs[formName].resetFields();
      },
      handleCancel(formName) {
        this.dialogUpdateVisible = false;
        this.$refs[formName].resetFields();
      },
      handleConfirm(formName) {
        console.log("updateData=" + JSON.stringify(this.updateData));
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.dialogUpdateVisible = false;
            this.$axios.put('/news_category/' + this.updateData.id + '/', {"name": this.updateData.name})
              .then(response => {
                console.log(response.data);
                if (response.status === 200 & response.data["id"] != null) {
                  this.$message.success('修改成功');
                  this.dialogUpdateVisible = false;
                  this.showNewsCategory()
                } else {
                  this.$message.error('修改失败');
                  this.dialogUpdateVisible = false;
                  this.showNewsCategory()
                }
              }).catch(function (error) {
              console.log(error);
            });
          }
        })
      },
      delNewsCategory(scope) {
        console.log("scope.row=" + JSON.stringify(scope.row));
        this.$confirm('确认是否删除', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning',
          center: true
        }).then(() => {
          this.$axios.delete('/news_category/' + scope.row.id + '/').then(response => {
            if (response.status === 204) {
              this.$message.success('删除成功');
              this.showNewsCategory()
            } else {
              this.$message.error("删除失败");
              this.showNewsCategory()
            }
          })
        }).catch(() => {
          this.$message.info("取消删除")
        })
      }
    }
  }
</script>

<style scoped>
</style>
