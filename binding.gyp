{
  'variables': {
      #
      # targets에서 사용할 수 있는 변수 선언
      # targets에서 <@(noderoot) 식으로 사용가능
      #
      'noderoot': '../../../'
  },
  'targets': [
    {
      #
      # 생성할 모듈이름 (modulename.node)
      #
      'target_name': 'utils',
      'sources': [ 'utils.cc' ],
      'conditions': [
        #
        # OS linux condition 추가
        #
        [ 'OS=="linux"', {
          #
          # unistd.h 들어있는 include_dir 추가
          # gethostname 함수 포함 파일
          #
          'include_dirs': [
            '/usr/include',
          ]
        } ]
      ]
    }
  ]
}