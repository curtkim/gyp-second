#include <node.h>
#include <v8.h>
//
// gethostname 함수 선언되어 있는 헤더
//
#include <unistd.h>
using namespace v8;
//
// hostname 가져오기
//
static Handle<Value> GetHostname(const Arguments& args) {
  HandleScope scope;
  char s[255];
  gethostname(s, 255);
  return scope.Close(String::New(s));
}
void init(Handle<Object> target) {
  //
  // property 설정
  //
  NODE_SET_METHOD(target, "getHostname", GetHostname);
}
NODE_MODULE(utils, init);