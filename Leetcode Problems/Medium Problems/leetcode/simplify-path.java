class Solution {
    public String simplifyPath(String path) {
        Stack<String> pathStack = new Stack<>();

        for(String p : path.split("/")){
            if(p.equals(".") || p.equals("")) continue;
            else if(p.equals("..")){
                if(!pathStack.isEmpty()) pathStack.pop();
            }
            else{
                pathStack.push(p);
            }
        }

        StringBuilder final_result = new StringBuilder();
        
        for(String dir: pathStack){
            final_result.append("/").append(dir);
        }


        return final_result.length() == 0 ? "/" : final_result.toString();
    }
}